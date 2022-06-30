# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    specific_lot_number = fields.Integer(string="Product Lot Number", default=None, readonly=True, force_save="1")

