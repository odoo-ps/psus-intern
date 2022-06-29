# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductLists(models.Model):
    _name = 'greenville.products_list'
    _description = 'Greenville Products List'

    name = fields.Char(string='Title', required=True)
    product_template_ids = fields.Many2many(
        'product.template', string='Product Template')
    customers_using_list = fields.One2many(
        'res.partner', 'products_list_id', string='Customers Using List')
