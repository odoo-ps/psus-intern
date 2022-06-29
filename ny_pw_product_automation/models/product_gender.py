# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductGender(models.Model):
    _name = 'nypw.product.gender'

    name = fields.Char(string='Name', required=True)
    upc_sequence = fields.Many2one(string='UPC Sequence', comodel_name='ir.sequence', required=True)
