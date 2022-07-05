# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class StockLocation(models.Model):
    _inherit = 'stock.location'

    external_id = fields.Integer(string="External ID")
    external_name = fields.Char(string="External Name")
