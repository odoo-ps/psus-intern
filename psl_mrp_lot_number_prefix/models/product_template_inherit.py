# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProductTemplateInherit(models.Model):

    _inherit = "product.template"
    
    lot_number_prefix = fields.Char(string='Lot Number Prefix')
