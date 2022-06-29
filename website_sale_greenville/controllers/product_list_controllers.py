from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domains = super(WebsiteSaleInherit, self)._get_search_domain(search, category, attrib_values, search_in_description)
        product_list_id = request.env.user.partner_id.product_list_id

        if product_list_id:
            domains.append(("id", "in", product_list_id.product_ids.ids))
        return domains
           