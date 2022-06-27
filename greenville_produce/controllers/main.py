# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute
from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSaleInherit(WebsiteSale):

    # Adds subdomain to search domain that filters products within users product list
    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domains = super(WebsiteSaleInherit,self)._get_search_domain(search, category, attrib_values, search_in_description)
        domains.append(('product_list_ids', '=', http.request.env.user.product_list_id.id))
        return domains
    