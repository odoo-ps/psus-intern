# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductList(models.Model):
    _name = "product.list"
    _description = "Customized list of products for display on the shop page"

    name = fields.Char(required=True)
    tag_ids = fields.Many2many(comodel_name="product.list.tag")
    product_ids = fields.Many2many(comodel_name="product.template")
    customer_ids = fields.One2many(comodel_name="res.partner", inverse_name="product_list_id")
