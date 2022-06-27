# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = "sale.order"

    expiration = fields.Datetime(string="Expiration")

# the auto-update cron job to run at midnight every day
    def _cancel_expired_orders(self):

        #recordset = self.search([("expiration","!=",False)]) #only return records with set expirations

        recordset = self.search([("expiration","!=",False)])        

        for record in recordset:
            if datetime.now().day > record.expiration.day: #if this day is past the expiration day
                    record.state = "cancel"
