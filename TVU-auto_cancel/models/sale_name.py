# -*- coding: utf-8 -*-
from odoo import fields, models, api 
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit='sale.order'
    
    def aotu_cancel_expired_quotation(self):
        today=fields.datetime.now()
        midnight='00:00:00'
        current_time=today.strftime("%X")
        if current_time==midnight:
            for order in self:
                if order.state not in ('draft','sent') and  order.validity_date < today:
                   order.action_cancel()
                            