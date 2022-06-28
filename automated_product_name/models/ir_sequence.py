# -*- coding: utf-8 -*-

from odoo import fields, models


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    category_id = fields.Many2one("product.template", string='category id', required=True)
    gender = fields.Char("product.template", string='product gender', required=True)