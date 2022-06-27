# coding: utf-8
from odoo import _
from odoo.exceptions import UserError
from odoo import http
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post)
        url = "/shop"
        if category:
            url = "/shop/category/%s" % slug(category)
        product_list_ = http.request.env['product.list'].search(
            [('customer_id', '=', http.request.env.user.partner_id.id)]).product_ids
        #if product_list_ is empty or not set, then show all products
        if not product_list_:
            return res

        pager_product_list = http.request.website.pager(url=url, total=len(
            product_list_), page=page, step=res.qcontext['ppg'], scope=7, url_args=post)
        # update values in res
        res.qcontext.update({
            'products': product_list_,
            'pager': pager_product_list,
            'bins': TableCompute().process(product_list_, res.qcontext['ppg'], res.qcontext['ppr']),
        })
        return res
