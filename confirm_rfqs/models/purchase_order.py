# *-* coding: utf-8 *-*
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def confirm_rfqs(self):
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('partner_id.id', '=',self.env.ref('base.main_partner').id ), ('user_id.id', '=', self.env.ref('base.user_admin').id)]):
            order.button_confirm()
