# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):

    _inherit = 'account.move'

    subscription_property_partner = fields.Many2one(comodel_name='res.partner', compute='_compute_property_partner', string='Property Partner', store=True, readonly=True)

    def __fetch_property_partner_from_subscription(self, invoice_origin):
        return self.env['sale.subscription'].search([('code','=',invoice_origin)]).property_partner


    @api.depends('subscription_property_partner')
    def _compute_property_partner(self):

        for rec in self:
            rec.subscription_property_partner = self.__fetch_property_partner_from_subscription(rec.invoice_origin)
