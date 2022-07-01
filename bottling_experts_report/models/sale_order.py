# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_studio_final_client = fields.Many2one(related="partner_id")
    x_studio_opportunity = fields.Char()  # service as a product
    x_studio_opportunity_desc = fields.Char()  # service as a product
    x_studio_travel_in = fields.Date()
    x_studio_travel_out = fields.Date()
