# -*- codign: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'
    name = fields.Char(string='Name', required=True)

    products_ids = fields.Many2many(comodel_name='product.template', string='Products')
    costumers_ids = fields.One2many(comodel_name='res.partner', string='Costumers', inverse_name='product_list_ids')
