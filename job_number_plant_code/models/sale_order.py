# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    job_number = fields.Char()
    job_sequence = fields.Char()

    plant_code = fields.Char()
    plant_sequence = fields.Char()
