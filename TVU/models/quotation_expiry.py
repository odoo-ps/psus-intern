# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import date, timedelta


class tvu_networks(models.Model):
    _inherit = 'sale.order'

    def auto_cancel_quotation_upon_expiry(self):
        
        filtered_table = self.search([  
                ('state', '=', 'draft'),
                ('validity_date', '!=', 'False'),
                ('validity_date', '<=', date.today())
            ])
        
        for record in filtered_table:
            record.action_cancel()