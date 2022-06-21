# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
import logging
logger = logging.getLogger(__name__)
class SaleQuotationExpiry(models.Model):
    _inherit='sale.order'
    
    #This function is called when the scheduler goes off
    def auto_cancel_expired_quotations(self):
        """
        This function is called to autocancel the quotations which are expired
        """
        record_set = self.search([('state','=','draft'),('validity_date','!=',False),('validity_date','<',date.today())])
        for record in record_set:
                record.update({
                        'state':'cancel'
                })
