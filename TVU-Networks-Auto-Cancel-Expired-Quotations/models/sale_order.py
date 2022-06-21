# -*- Coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  @api.autovacuum
  def _delete_expired_quotations(self):
    self.env['sale.order'].search([('validity_date', '<', fields.Date.today())]).write({'state': 'cancel'})
