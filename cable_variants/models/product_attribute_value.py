# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    code = fields.Char(string='Part identifier')
