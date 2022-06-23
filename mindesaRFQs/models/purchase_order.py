# -*- coding: utf-8 -*-

from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _confirm_rfq(self):
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('user_id.id', '=', '1'), ('partner_id.id', '=', '1')]):
            order.button_confirm()
