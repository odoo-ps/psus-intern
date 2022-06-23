# -*- coding: utf-8 -*-

from odoo import models
from datetime import date

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def cancel_expired_quotations(self):
        self.env['sale.order'].search([('state', '=', 'draft'),('validity_date', '!=', False),('validity_date','<',date.today())]).write({'state': 'cancel'})
