# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    property_partner = fields.Many2one("res.partner")

    # overwrite original function
    def _prepare_invoice_data(self):
        self.ensure_one()

        record = super()._prepare_invoice_data()
        # sets shipping addr as addr of current partner (if exists)
        # or leave it alone
        record['partner_shipping_id'] = self.property_partner.id or \
            record.get('partner_shipping_id')
        return record

    # overwrite original function
    def _prepare_renewal_order_values(self, discard_product_ids=False,
                                      new_lines_ids=False):
        record = super()._prepare_renewal_order_values(discard_product_ids,
                                                       new_lines_ids)
        # set shipping addr of subscriptions as addr of associated partner
        for subscription in self.filtered('property_partner'):
            record[subscription.id]['partner_shipping_id'] = \
                self.property_partner.id
        return record
