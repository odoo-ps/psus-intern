# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def action_cron_auto_confirm_rfqs(self):
        """
        This method is used to confirm RFQs automatically but only from Mindesa SAPI de CV
        """
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('partner_id.id', '=', '1'), ('user_id.id', '=', '2')]):
            order.button_confirm()
