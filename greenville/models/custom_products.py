# -*- coding: utf-8 -*-

from odoo import models, fields, api


class greenville(models.Model):
    _name = 'custom.products'
    _description = 'Custom Products List'

    product_list_name = fields.Char(string="Name", required=True)
    product_ids = fields.Many2many(comodel_name="product.template", string="Products")
    customer_ids = fields.One2many(comodel_name="res.partner", string="Customers", inverse_name='product_list', readonly=True)