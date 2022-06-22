# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SubscriptionSalePartner(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(comodel_name='res.partner',string="Property Partner")

    def _recurring_create_invoice(self, *args, **kwargs):
        print("Logged call")
        return super()._recurring_create_invoice(*args, **kwargs)

    