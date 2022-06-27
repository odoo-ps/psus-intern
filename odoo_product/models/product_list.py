# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ProductList(models.Model):

    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Title', required=True)
    product_ids = fields.Many2many(comodel_name='product.template',
                                   string='Product Template')
    customer_id = fields.One2many(comodel_name='res.partner',
                                  inverse_name='product_list_id',
                                  string='Customer Using This List')
