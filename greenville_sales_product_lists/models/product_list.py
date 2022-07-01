# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProductList(models.Model):
    _name = "product.list"
    _description = "Product List"

    name = fields.Char(string="Title", required=True)

    product_ids = fields.Many2many(
        comodel_name="product.product", string="Products on this List"
    )

    customer_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="product_list_ids",
        string="Customers using list",
    )
