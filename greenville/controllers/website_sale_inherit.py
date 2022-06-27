# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
# Import the class
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute
from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(
            page=0, category=None, search='', ppg=False, **post)
        product_list = http.request.env['product.list'].search(
            [('costumers_ids', '=', http.request.env.user.partner_id.id)]).products_ids
        if(product_list):
            url = "/shop"
            if category:
                url = "/shop/category/%s" % slug(category)
            pager_product_list = http.request.website.pager(url=url, total=len(
                product_list), page=page, step=res.qcontext['ppg'], scope=7, url_args=post)
            res.qcontext.update({'products': product_list,
                                'pager': pager_product_list,
                                 'bins': TableCompute().process(product_list, ppg, res.qcontext['ppr'])})
        return res
