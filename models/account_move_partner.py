# -*- coding: utf-8 -*-

from odoo import fields, models, api

class AccountMovePartner(models.Model):
    _inherit = 'account.move'

    prop_partner = fields.Many2one(comodel_name='res.partner', string="Property Partner")

    def _get_invoice_delivery_partner_id(self):
        if self.prop_partner:
            self.ensure_one()
            return self.prop_partner.address_get(['delivery'])['delivery']
        else:
            return super()._get_invoice_delivery_partner_id()