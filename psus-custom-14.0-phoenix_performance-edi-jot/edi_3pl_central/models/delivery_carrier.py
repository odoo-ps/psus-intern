# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    carrier_name = fields.Char(string='Carrier Name')
    billing_code = fields.Char(string='Billing Code')