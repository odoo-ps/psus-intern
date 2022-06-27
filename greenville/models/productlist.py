# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductList (models.Model):
    _name = 'productlist'

    name = fields.Char(string='Name', required=True)
   
    product_ids = fields.Many2many(comodel_name='product.template', string='Products Template')
    customer_ids = fields.One2many(comodel_name='res.partner', string='Costumers Using List', inverse_name="list_ids")
