# -*- coding: utf-8 -*-

from odoo import api, fields, models

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"
  
  def confirm_rfqs(self):
    orders = self.env['purchase.order'].search([
      ('state', '=', 'draft'), 
      ('user_id.id', '=', 2), 
      ('partner_id.id', '=', 1)
    ])
    for order in orders:
      order.button_confirm()
