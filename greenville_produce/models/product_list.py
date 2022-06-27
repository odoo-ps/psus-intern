# *-* coding: utf-8 *-*
from odoo import models,fields,api


class ProductList(models.Model):
    _name="product.list"
    
    name=fields.Char(string='Product List', required=True)
    product_ids = fields.Many2many(comodel_name="product.template", inverse_name="product_list_ids")
    user_ids= fields.One2many('res.partner', inverse_name="product_list_id",string='Users')
