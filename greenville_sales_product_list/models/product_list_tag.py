# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductListTag(models.Model):
    _name = "product.list.tag"
    _description = "Product tags"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    sql_constraints = [
        ("unique_product_tag", "UNIQUE(name)", "Product tags must be unique")
    ]
