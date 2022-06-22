# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SubscriptionSalePartner(models.Model):
    _inherit = 'sale.subscription'

    prop_partner = fields.Many2one(comodel_name='res.partner',string="Property Partner")

    def _recurring_create_invoice(self, *args, **kwargs):
        invoices = super()._recurring_create_invoice(*args, **kwargs)
        
        for invoice in invoices:
            if self.prop_partner:
                invoice.update({'prop_partner': self.prop_partner})

        return invoices

    