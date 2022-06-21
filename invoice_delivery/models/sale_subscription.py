# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(comodel_name='res.partner',
                                       string='Property Partner')

    @api.onchange('property_partner')
    def change_shipping_id(self):
        self.ensure_one()
        if self.property_partner:
            delivery_address = self.property_partner.address_get(
                ['delivery', 'invoice'])['delivery']
            self.write({'partner_shipping_id': delivery_address})
        else:
            delivery_address = self.partner_id.address_get(
                ['delivery', 'invoice'])['delivery']
            self.write({'partner_shipping_id': delivery_address})
