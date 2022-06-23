# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def _confirm(self):
        if self.state in {'draft', 'sent'}:
            self.state = 'purchase'

    def _auto_confirm_rfqs(self):
        internal_rfqs = self.search([
            ('state', '=', 'draft'),
            ('partner_id', '=', 1),
            ('user_id', '=', 1)
        ])
        for rfq in internal_rfqs:
            rfq._confirm()