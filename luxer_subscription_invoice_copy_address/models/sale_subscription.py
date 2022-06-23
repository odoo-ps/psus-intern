# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one('res.partner', string='Property partner')

    def _prepare_invoice(self):
        self.ensure_one()
        invoice = super()._prepare_invoice()
        if self.property_partner:
            invoice['partner_shipping_id'] = self.property_partner.id
        return invoice
