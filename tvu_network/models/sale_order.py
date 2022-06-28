# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.autovacuum
    def _autocancel_expired_quotations(self):
        for sale in self.env['sale.order'].search([]).filtered(lambda s: ((s.validity_date and s.validity_date < fields.Date.today()) or s.is_expired)):
            sale.action_cancel()
            
