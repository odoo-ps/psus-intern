# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SubscriptionSalePartner(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(comodel_name='res.partner',string="Property Partner")

    def _recurring_create_invoice(self, *args, **kwargs):
        invoices = super()._recurring_create_invoice(*args, **kwargs)
        
        for invoice in invoices:
            if self.property_partner:
                # invoice delivery address managed by partner_id
                # or add aditional delivery_address field to invoice and hook _get_invoice_delivery_partner_id
                # ticket not specific enough
                invoice.update({'partner_id': self.property_partner})

        return invoices

    