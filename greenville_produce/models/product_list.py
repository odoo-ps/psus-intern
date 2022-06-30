# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductList(models.Model):

    _name = 'greenville.products.list'
    _description = 'description'

    name = fields.Char('Test Name', required=True)
    greenville_products_id = fields.Many2many(comodel_name="product.product", string="Product Template")

    greenville_customers_id = fields.One2many(comodel_name="res.partner", inverse_name="product_list_id", string="Customers List")

