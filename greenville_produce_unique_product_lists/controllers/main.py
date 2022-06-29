# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        search_domain = super()._get_search_domain(search, category, attrib_values, search_in_description)
        products_list_id = request.env.user.partner_id.products_list_id
        if products_list_id:
            search_domain = [('id', 'in', products_list_id.product_template_ids.ids), *search_domain]
        return search_domain
