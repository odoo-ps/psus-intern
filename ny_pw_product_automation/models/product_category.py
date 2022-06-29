# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    sequence = fields.Many2one(string='Sequence', comodel_name='ir.sequence', required=True)