# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger = logging.getLogger(__name__)

#class ProductList(http.Controller):
class WebsiteSaleInherit(WebsiteSale):
    #@http.route("/shop/", auth="public", website=True)
    @http.route()
    def shop(self, **kw):
        products = http.request.env["product.list"].search([])
        res=super().shop()
        user=http.request.env.user.partner_id.id
        _logger.critical("User ID: " + str(user))
        #_logger.critical(res)

        #product_lists = http.request.env['product.list'].search([])

        product_list = http.request.env['product.list'].search([('customer_ids','=',user)]) #contains the list ID of the user (If there is one)

        

        if (product_list):
            _logger.critical("TRUE")
            _logger.critical("List ID: " + product_list.name)
            #res.qcontext.update({"products:", product_list})
            context = dict(http.request.context)
            context.update({"products" : product_list})
            http.request.context=context
        else:
            _logger.critical("false")


        

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
        #return "hi there :)"