# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Quotations(models.Model):

    _inherit = 'sale.order'
    
    def cancel_expired_quotations(self):

        records = self.search([('state','=','draft')])

        for i in records:
            i.action_cancel()
