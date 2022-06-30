from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from ..models import unique_product_list

class WebsiteSaleInherit(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        res = super(WebsiteSaleInherit, self)._get_search_domain( search, category, attrib_values, search_in_description=True)
        product_list = request.env.user.partner_id.product_list_to_customers.product_lists
        if product_list:
            res.append(('id', 'in', request.env.user.partner_id.product_list_to_customers.product_lists.ids ) )
        return res