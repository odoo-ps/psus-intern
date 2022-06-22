# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import date, timedelta


class tvu_networks(models.Model):
    _inherit = 'sale.order'

    def check_expiry(self):
        
        filtered_table = self.search([('state', '=', 'draft')])
        
        for record in filtered_table:
            if not record.validity_date:
                continue
            elif record.validity_date - date.today() <= timedelta(days=0):
                record.update({
                    'state': 'cancel'
                })