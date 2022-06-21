# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _cancel(self):
        if self.state in {'draft', 'sent'}:
            self.state = 'cancel'

    def _auto_cancel_expired(self):
        records = self.search([
            ('state', 'in', ['draft', 'sent']),
            ('validity_date', '<', fields.Date.today())
        ])
        for record in records:
            record._cancel()
