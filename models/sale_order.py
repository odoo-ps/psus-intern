# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class SaleOrder(models.Model):

    _inherit = 'sale.order'
    
    def cancel_expired_quotations(self):

        records = self.search([
            ('state','=','draft'),
            ('validity_date', '!=', 'False'),
            ('validity_date', '<=', date.today())
            ])

        for record in records:
            record.action_cancel()
