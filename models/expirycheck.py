# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExpiryCheck(models.Model):
    _name = 'sale_tvu_expiry.expiry_check'
    _description = 'Expiry Check'


    def check_records(self):
        sales = self.env['sale.order']
        today = fields.Date.today()
        
        expired_records = sales.search([('validity_date','!=',False),('state','=','draft'),('validity_date','<',today)])
        for record in expired_records:
            record.update({'state': 'cancel'})
            # print("canceled record", record.name)
    
