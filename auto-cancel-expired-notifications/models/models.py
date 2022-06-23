# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def auto_cancel_expired(self): 
        """
        Auto cancel all expired quotation where validity/expiry date is less than current date.
        To be run once daily.
        """
        records = self.env['sale.order'].search([('state', '=', 'draft'),
                ('validity_date', '<', date.today()),
                ('validity_date', '!=', False)])

        for record in records:
            record.action_cancel()
            
