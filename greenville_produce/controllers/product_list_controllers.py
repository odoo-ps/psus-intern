# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.osv import expression

class ProductList(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        user_id = http.request.env.user.partner_id.id

        super_doms = super()._get_search_domain(search, category, attrib_values, search_in_description)
        product_list = http.request.env['product.list'].search([('customer_ids', '=', user_id)])
        if len(product_list) == 0:
            #return all products if product list is empty (for this user)
            return super_doms
        else:
            return expression.AND([super_doms, [('customer_ids', '=', user_id)]])
