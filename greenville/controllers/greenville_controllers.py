# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger = logging.getLogger(__name__)

#class ProductList(http.Controller):
class WebsiteSaleInherit(WebsiteSale):
    #@http.route("/shop/", auth="public", website=True)
    @http.route()
    #def shop(self, category=None, search="", **kw):
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post): #taken from the inherited func in odoo/addons/website_sale/controllers/main.py
        #products = http.request.env["product.list"].search([])
        res=super(WebsiteSaleInherit, self).shop(page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg)

        user=http.request.env.user.partner_id.id
        _logger.critical("User ID: " + str(user))
        #_logger.critical(res)

        #product_lists = http.request.env['product.list'].search([])

        #product_list = http.request.env['product.list'].search([('customer_ids','=',user)]) #contains the list ID of the user (If there is one)
        product_list = http.request.env['res.partner'].search([("id","=",user)]).product_list_id
        
        context = dict(http.request.context)

        _logger.critical(str(http.request.context))

        if (product_list):
            _logger.critical("TRUE")
            _logger.critical("List name: " + product_list.name)
            #res.qcontext.update({"products:", product_list})
            #context = dict(http.request.context)
            
            _logger.critical("IDs: " + str(product_list.product_ids))

            for product in product_list.product_ids:
                _logger.critical("Product name: " + product.name)
            #res.qcontext.update({"products" : product_list.product_ids})
            context["products"] = product_list.product_ids
            http.request.context=context

        else:
            _logger.critical("false")

        #Product_list now contains the products in the product list that this person is using.

        

        """
        for record in product_lists:
            _logger.critical("New list")
            for prodlist in record:
                products = prodlist.product_ids.search([])
                _logger.critical("List: " + prodlist.name)

                customers = prodlist.customer_ids.search([])
                
                for customer in customers:
                    _logger.critical("Customer: " + str(customer.name))

                for product in products:
                    _logger.critical("product " + str(product.name))
                #_logger.critical("Is this customer in this list: ", str(user == prodlist.customer_ids.id))
        """
        
        
        return res
        #return http.request.render("website_sale.products",{"products":product_list.product_ids, "category":category})
        #return http.request.render("website_sale.products",context)
        #return "hi there :)"