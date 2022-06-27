# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

from datetime import date

logger = logging.getLogger(__name__)

class tvu(models.Model):
    _inherit = "sale.order"

    def AutoCancelExpiredQuotations(self):
        today = date.today()
        d1 = today.strftime("%Y-%m-%d") # datetime right now 
        # logger.info("Auto Cancel Expired Quotations")
        # ids that are expired quotations.
        # it skips those ids whose expiration date are not set. 
        ids = self.env['sale.order'].search([['validity_date','<=',d1],['state','=','draft']])
        for id in ids:
            id.state = 'cancel'
