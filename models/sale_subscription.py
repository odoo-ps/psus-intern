# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleSubscription(models.Model):

    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(comodel_name='res.partner', string='Property Partner', store=True)

    @api.onchange('property_partner')
    def update_invoice(self):

        invoices = self.env['account.move'].search([('invoice_origin','=',self.code)])

        for rec in invoices:
            rec.subscription_property_partner = self.property_partner
