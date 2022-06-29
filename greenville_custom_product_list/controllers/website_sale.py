from requests import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo import models,fields,api,http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
from werkzeug.exceptions import Forbidden, NotFound
from odoo.addons.website.controllers.main import QueryURL
class WebsiteSaleInherit(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        res = super(WebsiteSaleInherit,self)._get_search_domain(search, category, attrib_values, search_in_description=True)
        prod_list = request.env.user.partner_id.product_list_name_id.product_list_id
        if prod_list:
            res.append(('id','in',request.env.user.partner_id.product_list_name_id.product_list_id))
        print(res)
        return res