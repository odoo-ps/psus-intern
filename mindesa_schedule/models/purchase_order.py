# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _confirmRPQ(self):
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('partner_id.id', '=', '1'), ('user_id.id', '=', '1')]):
            order.button_confirm()
