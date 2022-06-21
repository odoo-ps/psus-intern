# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _, SUPERUSER_ID


class Subscription(models.Model):
    _inherit = 'sale.subscription'

    property_partner_id = fields.Many2one(
        comodel_name='res.partner', string='Property Partner')

    def _prepare_invoice_data(self):
        self.ensure_one()
        vals = super()._prepare_invoice_data()
        vals['partner_shipping_id'] = self.property_partner_id or vals.get(
            'partner_shipping_id')
        return vals

    def _prepare_renewal_order_values(self, discard_product_ids=False, new_lines_ids=False):
        res = super()._prepare_renewal_order_values(discard_product_ids, new_lines_ids)
        for subscription in self.filtered('property_partner_id'):
            res[subscription.id]['partner_shipping_id'] = self.property_partner_id.id
        return res
