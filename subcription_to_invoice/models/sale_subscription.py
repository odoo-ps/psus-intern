# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleSubscription(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    partner = fields.Many2one('res.partner', 'Contact')

    def create_invoices(self):
        data = super(SaleSubscription, self)._prepare_invoice_data()
        if self.partner:
            data['partner_shipping_id'] = self.partner.id
        return super(SaleSubscription, self).create_invoices()