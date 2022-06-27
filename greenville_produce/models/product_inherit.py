# *-* coding: utf-8 *-*
from odoo import models, fields, api


class Product(models.Model):
    _inherit="product.template"
    
    product_list_ids=fields.Many2many(comodel_name="product.list", inverse_name="product_ids")
