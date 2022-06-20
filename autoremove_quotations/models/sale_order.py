# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
           
    @api.autovacuum
    def remove_quotation_if_expired_autovacuum(self):
        for record in self:
            if record.validity_date and record.type_name=='Quotation':
                if record.is_expired or record.validity_date < fields.Date.today():
                    record.state='cancelled'