# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute

#class ProductList(http.Controller):
class WebsiteSaleInherit(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        # ^^ parms taken from the inherited func in odoo/addons/website_sale/controllers/main.py

        res=super(WebsiteSaleInherit, self).shop(page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg)
        qcontext = res.qcontext

        user=http.request.env.user.partner_id.id

        product_list = http.request.env['res.partner'].search([("id","=",user)]).product_list_id
        # ^^ finds the current user's id, then retrieves the many2one field that contains the product list for that user
        
    
        # if the user is using a product list, update the qcontext to only display the products on the list
        if product_list:
            qcontext["products"] = product_list.product_ids

            ppr = http.request.env['website'].get_current_website().shop_ppr or 4
            # ^^ from odoo/addons/website_sale/controllers/main.py in WebsiteSale.shop()

            qcontext["bins"] = TableCompute().process(product_list.product_ids, ppg, ppr) 
            # ^^ re-generate the table that displays the products with the new product list


        #render the webpage using our newly updated qcontext
        return http.request.render("website_sale.products",qcontext=qcontext)