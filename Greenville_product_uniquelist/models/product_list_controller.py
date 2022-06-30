# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductList(WebsiteSale):

    
    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domain = super(ProductList, self)._get_search_domain(search, category, attrib_values, search_in_description)
        product_list_id = http.request.env.user.partner_id.product_list_id
        if product_list_id:
            domain.append([('id', 'in', product_list_id.product_list.ids)])
        return domain
        
