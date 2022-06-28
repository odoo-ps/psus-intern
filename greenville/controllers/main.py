import json
import logging
from datetime import datetime

from odoo import SUPERUSER_ID, _, fields, http, tools
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.addons.website.controllers.main import QueryURL, Website
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_sale.controllers.main import TableCompute, WebsiteSale
from odoo.exceptions import ValidationError
from odoo.http import request
from odoo.osv import expression
from werkzeug.exceptions import Forbidden, NotFound

_logger = logging.getLogger(__name__)

# This controller inherits @WebsiteSale
# to control product visibility based on res.partner's pricelist
class WebsiteSaleInherit(WebsiteSale):

    # method necessary for shop controller.
    def sitemap_shop(env, rule, qs):
        if not qs or qs.lower() in "/shop":
            yield {"loc": "/shop"}

        Category = env["product.public.category"]
        dom = sitemap_qs2dom(qs, "/shop/category", Category._rec_name)
        dom += env["website"].get_current_website().website_domain()
        for cat in Category.search(dom):
            loc = "/shop/category/%s" % slug(cat)
            if not qs or qs.lower() in loc:
                yield {"loc": loc}

    # A controller inherited from WebsiteSale.shop.
    # if current user has product lists selected,
    # the controller will show only the products that are in user's product lists.
    @http.route(
        [
            """/shop""",
            """/shop/page/<int:page>""",
            """/shop/category/<model("product.public.category"):category>""",
            """/shop/category/<model("product.public.category"):category>/page/<int:page>""",
        ],
        type="http",
        auth="public",
        website=True,
        sitemap=sitemap_shop,
    )
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        add_qty = int(post.get("add_qty", 1))
        Category = request.env["product.public.category"]
        if category:
            category = Category.search([("id", "=", int(category))], limit=1)
            if not category or not category.can_access_from_current_website():
                raise NotFound()
        else:
            category = Category

        if ppg:
            try:
                ppg = int(ppg)
                post["ppg"] = ppg
            except ValueError:
                ppg = False
        if not ppg:
            ppg = request.env["website"].get_current_website().shop_ppg or 20

        ppr = request.env["website"].get_current_website().shop_ppr or 4

        attrib_list = request.httprequest.args.getlist("attrib")
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attributes_ids = {v[0] for v in attrib_values}
        attrib_set = {v[1] for v in attrib_values}

        domain = self._get_search_domain(search, category, attrib_values)

        keep = QueryURL(
            "/shop",
            category=category and int(category),
            search=search,
            attrib=attrib_list,
            order=post.get("order"),
        )

        pricelist_context, pricelist = self._get_pricelist_context()

        request.context = dict(
            request.context, pricelist=pricelist.id, partner=request.env.user.partner_id
        )

        url = "/shop"
        if search:
            post["search"] = search
        if attrib_list:
            post["attrib"] = attrib_list

        Product = request.env["product.template"].with_context(bin_size=True)
        search_product = Product.search(domain, order=self._get_search_order(post))

        # <---------------->
        # Added following lines to filter products based on res.partner's product_lists
        product_lists = request.env.user.partner_id.parent_id.product_list
        # if user has product lists
        if product_lists:
            product_tmpl_ids = []
            for product in product_lists.products:
                product_tmpl_ids.append(product.product_tmpl_id.id)
            products = request.env["product.template"].search(
                [("id", "in", product_tmpl_ids)]
            )
            search_product = products
        # <----------------->
        website_domain = request.website.website_domain()
        categs_domain = [("parent_id", "=", False)] + website_domain
        if search:
            search_categories = Category.search(
                [("product_tmpl_ids", "in", search_product.ids)] + website_domain
            ).parents_and_self
            categs_domain.append(("id", "in", search_categories.ids))
        else:
            search_categories = Category
        categs = Category.search(categs_domain)

        if category:
            url = "/shop/category/%s" % slug(category)

        product_count = len(search_product)
        pager = request.website.pager(
            url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post
        )
        offset = pager["offset"]
        products = search_product[offset : offset + ppg]
        ProductAttribute = request.env["product.attribute"]
        if products:
            # get all products without limit
            attributes = ProductAttribute.search(
                [("product_tmpl_ids", "in", search_product.ids)]
            )
        else:
            attributes = ProductAttribute.browse(attributes_ids)

        layout_mode = request.session.get("website_sale_shop_layout_mode")
        if not layout_mode:
            if request.website.viewref("website_sale.products_list_view").active:
                layout_mode = "list"
            else:
                layout_mode = "grid"

        values = {
            "search": search,
            "category": category,
            "attrib_values": attrib_values,
            "attrib_set": attrib_set,
            "pager": pager,
            "pricelist": pricelist,
            "add_qty": add_qty,
            "products": products,
            "search_count": product_count,  # common for all searchbox
            "bins": TableCompute().process(products, ppg, ppr),
            "ppg": ppg,
            "ppr": ppr,
            "categories": categs,
            "attributes": attributes,
            "keep": keep,
            "search_categories_ids": search_categories.ids,
            "layout_mode": layout_mode,
        }
        if category:
            values["main_object"] = category

        return request.render("website_sale.products", values)
