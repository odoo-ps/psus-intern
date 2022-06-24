# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleSubscription(models.Model):

    _inherit = 'sale.subscription'

    subscription_content = fields.Many2one(comodel_name='res.partner', string='Property Partner')

    @api.onchange('subscription_content')
    def _set_delivery_address(self):
        self.ensure_one()
        invoice = super()._prepare_invoice()
        if self.subscription_content:
            invoice['partner_shipping_id'] = self.subscription_content