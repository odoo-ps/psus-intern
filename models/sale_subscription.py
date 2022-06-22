# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SubscriptionSale(models.Model):
    _inherit = 'sale.subscription'

    property_partner = fields.Many2one(comodel_name='res.partner',string="Property Partner")

    