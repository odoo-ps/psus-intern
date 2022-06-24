# -*- coding: utf-8 -*-

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _confirm_rfqs(self):
        self.search([('state', '=', 'sent'),('partner_id', '=', 1),('user_id', '=', 1)]).button_confirm()