# -*- coding: utf-8 -*-

from odoo import models

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"
  
  def confirm_rfqs(self):
    odoobot = self.env.ref('base.partner_root')
    partner = self.env['res.partner'].find_or_create('info@yourcompany.com')
    orders  = self.env['purchase.order'].search([
      ('user_id.id','=',odoobot.id),
      ('partner_id.id','=',partner.id)
    ])
    for order in orders:
      if order.state == 'draft':
        order.button_confirm()
      else:
        continue
    
