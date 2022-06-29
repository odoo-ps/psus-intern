# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

#class ProductList(http.Controller):
class WebsiteSaleInherit(WebsiteSale):
    #@http.route("/shop/", auth="public", website=True)
    @http.route()
    def shop(self, **kw):
        products = http.request.env["product.list"].search([])
        return "Hello there :)"