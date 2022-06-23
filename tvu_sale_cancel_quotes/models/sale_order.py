# -*- coding: utf-8 -*-

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def cancel_expired_quotations(self):
        quotes = self.env['sale.order'].search([('state', '=', 'draft'),('validity_date', '!=', False),('is_expired', '=', True)]).write({'state': 'cancel'})
