# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Name', required=True)
    products = fields.Many2many(string='Product List', comodel_name='product.template')
    customers = fields.One2many(string='Customers That Use This List', comodel_name='res.partner',
                            inverse_name='product_list_id')
