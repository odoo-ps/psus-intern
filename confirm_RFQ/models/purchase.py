# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def confirm_RFQ(self):
        # NOTE: Maybe add the states 'sent' and 'to approve'
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('partner_id.id', '=', 1), ('user_id.id', '=', 1)]):
            order.button_confirm()
