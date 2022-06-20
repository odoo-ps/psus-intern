# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.autovacuum
    def _cancel_quotations(self):
        self.env['sale.order'].search([('validity_date', '<', fields.Date.today())]).action_cancel()
