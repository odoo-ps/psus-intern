# -*- Coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  @api.autovacuum
  def _delete_expired_quotations(self):
    self.env['sale.order'].search([('validity_date', '<', fields.Date.today())]).write({'state': 'cancel'})
