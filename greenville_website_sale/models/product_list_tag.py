# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductListTag(models.Model):
    _name = 'product.list_tag'

    name = fields.Char(string='Name', required=True)
    product_list_id = fields.Many2many('product.list', string='Product List')
