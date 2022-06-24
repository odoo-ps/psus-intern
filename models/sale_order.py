# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):

    _inherit = 'sale.order'
    
    def cancel_expired_quotations(self):

        records = self.search([('state','=','draft')])

        for record in records:
            record.action_cancel()
