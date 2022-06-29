# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_number_prefix = fields.Char('Lot Number Prefix')
