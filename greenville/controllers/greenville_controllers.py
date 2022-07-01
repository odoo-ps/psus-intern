# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import http
from odoo.http import request
from odoo.osv import expression
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSaleInherit(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        # ^^ parms taken from the inherited func in odoo/addons/website_sale/controllers/main.py

        res=super(WebsiteSaleInherit, self).shop(page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg)

        # ******** from inherited func
        url = "/shop"
        if category:
            url = '/shop/category/%s' % slug(category)
        # *******************

        user=request.env.user.partner_id.id

        product_list = request.env['res.partner'].search([("id","=",user)]).product_list_id
        # ^^ finds the current user's id, then retrieves the many2one field that contains the product list for that user
        
    
        # if the user is using a product list, update the qcontext to only display the products on the list
        if product_list:

            res.qcontext.update({"products":product_list.product_ids})

            ppr = request.env['website'].get_current_website().shop_ppr or 4
            # ^^ from odoo/addons/website_sale/controllers/main.py in WebsiteSale.shop()

            res.qcontext.update({"bins":TableCompute().process(product_list.product_ids, ppg, ppr)})
            # ^^ re-generate the table that displays the products with the new product list

            res.qcontext.update({"pager":request.website.pager(url=url, total=len(product_list.product_ids), page=page, step=res.qcontext['ppg'], scope=7, url_args=post)})
            # ^^ re-generate the pager to accomodate the new list

            res.qcontext.update({"search_count":len(product_list.product_ids)})

        return res
