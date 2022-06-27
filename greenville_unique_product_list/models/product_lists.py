# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductList(models.Model):
    _name = 'product.list'

    name = fields.Char(string='Name')

    customer_ids = fields.One2many(comodel_name='res.partner', inverse_name='product_list_id', string='Customers')

    product_ids = fields.Many2many(comodel_name='product.template', string="Products")
