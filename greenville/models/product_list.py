# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductList(models.Model):
    _name = "product.list"
    _description = "Product List"

    name = fields.Char(string="Title",required=True)

    #products that are on this list
    product_ids = fields.Many2many(comodel_name="product.template",
                                    string="Products on this list")

    #customers who are using this list
    customer_ids = fields.One2many(comodel_name="res.partner",inverse_name="product_list_id",string="Customers using list")
