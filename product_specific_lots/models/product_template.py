# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_prefix = fields.Char(string='Lot Number Prefix')
