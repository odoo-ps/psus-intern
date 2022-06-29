# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        uid = http.request.env.context.get('uid')
        user = http.request.env['res.users'].browse(uid)
        p = user.partner_id
        product_list = p.product_list_id
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        if product_list:
            if product_list.products:
                url = "/shop"
                if category:
                    url = "/shop/category/%s" % slug(category)

                if ppg:
                    try:
                        ppg = int(ppg)
                        post['ppg'] = ppg
                    except ValueError:
                        ppg = False
                if not ppg:
                    ppg = request.env['website'].get_current_website().shop_ppg or 20

                ppr = request.env['website'].get_current_website().shop_ppr or 4

                product_count = len(product_list.products)
                pager = request.website.pager(url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post)

                res.qcontext.update({'products': product_list.products,
                                     'pager': pager,
                                     'bins': TableCompute().process(product_list.products, ppg, ppr)})
        return res
