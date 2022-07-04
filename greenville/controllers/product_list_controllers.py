# -*- coding: utf-8 -*-

from odoo import http
from odoo.exceptions import UserError
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute

class WebsiteSaleInherit(WebsiteSale):
  
  @http.route('/shop', type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
  def shop(self, page=0, category=None, search='', ppg=False, **post):
    res = super(WebsiteSaleInherit, self).shop(page=page, category=category, search=search, ppg=ppg, **post)
    url = "/shop"
    products_list_req = http.request.env['product.list'].search(
      [('customer','=',http.request.env.user.partner_id.id)]
    ).products

    if not products_list_req:
      return res

    pager_product_list = http.request.website.pager(url=url, total=len(products_list_req), page=page, step=res.qcontext['ppg'], scope=7, url_args=post)

    res.qcontext.update({
      'products': products_list_req,
      'pager': pager_product_list,
      'bins': TableCompute().process(products_list_req,res.qcontext['ppg'],res.qcontext['ppr'])
    })

    return res
