# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ProductLists(models.Model):
    _name = 'greenville.products_list'
    _description = 'some description'

    name = fields.Char(string='Title', required=True)
    product_template_ids = fields.Many2many(
        'product.product', string='Product Template')
    customers_using_list = fields.One2many(
        'res.partner', 'products_list_id', string='Customers Using List', auto_join=True)
