# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cancel(models.Model):
    _inherit = 'sale.order'

    #check if the quotation is expired
    @api.autovacuum
    def check_expired(self):
        for record in self:
            if record.type_name == 'Quotation':
                if record.validity_date:
                    if(record.validity_date < fields.Date.today() or record.is_expired):
                        record.state = 'cancel'
                        record.is_expired = True
    
