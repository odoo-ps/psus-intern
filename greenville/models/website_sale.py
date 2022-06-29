# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleInherit(WebsiteSale):

    def _get_search_domain(self, *args):
        res = super(WebsiteSaleInherit, self)._get_search_domain(*args)
        prod_list_id = request.env.user.partner_id.product_list
        if prod_list_id:
            res.append(('id', 'in', prod_list_id.product_ids.ids))
        return res