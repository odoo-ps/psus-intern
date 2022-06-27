# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.order'

    def _confirm_rfqs(self):
        self.search([
            ('state', '!=', 'draft'),
            ('partner_id', '=', 1),
            ('user_id', '=', 1)
        ]).button_confirm()

