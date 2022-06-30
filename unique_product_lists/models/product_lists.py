# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Name', required=True)
    product_ids = fields.Many2many('product.template', string='Products')
    partner_ids = fields.One2many('res.partner', 'product_list_id',
                                  string='Customers')
    tag_ids = fields.Many2many('product.list_tag', string='Tags')
