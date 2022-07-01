# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    def _get_search_domain(
        self, search, category, attrib_values, search_in_description=True
    ):

        domains = super(WebsiteSaleInherit, self)._get_search_domain(
            search, category, attrib_values, search_in_description
        )
        product_list_ids = request.env.user.partner_id.product_list_ids

        if product_list_ids:
            domains.append(("id", "in", product_list_ids.product_ids.ids))
        return domains
