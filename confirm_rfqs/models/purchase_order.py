# *-* coding: utf-8 *-*
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def confirm_rfqs(self):
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('user_id.id', '=', 1), ('partner_id.id', '=', 1)]):
            order.button_confirm()
