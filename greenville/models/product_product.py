# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    #_name="product.product"
    _inherit="product.product"

    product_list_ids = fields.Many2many(comodel_name="product.list",
                                        string="Lists that this Product appears in")
                                        