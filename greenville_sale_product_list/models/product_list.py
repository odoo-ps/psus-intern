# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Name', required=True)
    product_id = fields.Many2many('product.product', string='Products')
    customer_id = fields.One2many('res.partner', 'product_list_id', string='Customers')
    