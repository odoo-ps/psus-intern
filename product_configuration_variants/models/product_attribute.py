# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductAtrribute(models.Model):
    _inherit = 'product.attribute.value'

    code = fields.Char(string="Code")
    