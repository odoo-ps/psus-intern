# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Name', required=True)
    # to be finished: Tags

    product_ids = fields.Many2many(comodel_name='product.template',
                                   string='Product List')

    customer_ids = fields.One2many(comodel_name='res.partner',
                                   inverse_name='product_list_id',
                                   string='Customers That Use This List')
