# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime
from datetime import timedelta
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    expiration = fields.Datetime(string="Expiration")

# the auto-update cron job to run at midnight every day
    def _cancel_expired_orders(self):
        _logger.error("Calling cancel expired orders")
        _logger.error(type(self))

        recordset = self.search([("expiration","!=",False)]) #only return records with set expirations
        

        for record in recordset:
            if datetime.now().day > record.expiration.day: #if this day is past the expiration day
                    record.state = "cancel"

