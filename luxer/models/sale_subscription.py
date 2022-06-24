# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(string='Property Partner', comodel_name='res.partner')

    def _prepare_invoice_data(self):
        invoice_data = super()._prepare_invoice_data()
        if self.property_partner:
            invoice_data.partner_shipping_id = self.property_partner.id

        return invoice_data

    def _prepare_renewal_order_values(self, discard_product_ids=False, new_lines_ids=False):
        invoice_data = super()._prepare_renewal_order_values(discard_product_ids, new_lines_ids)

        for subscription in self:
            if subscription.property_partner:
                invoice_data[subscription.id]['partner_shipping_id'] = subscription.property_partner.id

        return invoice_data

