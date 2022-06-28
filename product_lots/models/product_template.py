# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_number_prefix = fields.Char(string='Lot Number Prefix', default="00")
   