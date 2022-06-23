# -*- coding: utf-8 -*-

from odoo import models

MINDESA_PARTNER_ID = 1


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _confirm_store_rfqs(self):
        self.search([
            ('state', '!=', 'draft'),
            ('partner_id', '=', MINDESA_PARTNER_ID),
            ('user_id', '=', 1)  # OdooBot
        ]).button_confirm()
