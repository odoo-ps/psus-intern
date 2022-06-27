# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import res_partner


class ProductList(models.Model):
    _name = "product.list"
    _description = "Product List"

    name = fields.Char(string="Title",required=True)

    product_ids = fields.Many2many(comodel_name="product.product",
                                    string="Products on this List")
                                    #inverse_name="product_list_ids")

    """customer_ids = fields.One2many(comodel_name="res.partner",
                                    string="Customers using this List",
                                    inverse_name="product_list_ids")"""


    customer_ids = fields.One2many(comodel_name="res.partner",inverse_name="product_list_ids",string="Customers using list")