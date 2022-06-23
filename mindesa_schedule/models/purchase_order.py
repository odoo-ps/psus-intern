# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _confirm_rfq(self):
        print(self.env.uid)
        for order in self.env['purchase.order'].search([('state', '=', 'draft'),
                                                        ('partner_id.id', '=', self.env.ref('base.main_partner').id),
                                                        ('user_id.id', '=', self.env.ref('base.user_admin').id)]):
            order.button_confirm()
