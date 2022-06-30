# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):

        res = super(WebsiteSaleInherit, self).shop()

        current_user = request.env['res.users'].browse(request.uid).partner_id
        product_list = current_user.product_list_id

        if product_list:
            res.qcontext.update({"products": list(product_list.product_ids)})   # Update the products to the user's product list
            res.qcontext.update({"bins": TableCompute().process(    # Recompute the bins with the product list
                res.qcontext.get("products"), 
                res.qcontext.get("ppg"),
                res.qcontext.get("ppr")
            )})

        return res
