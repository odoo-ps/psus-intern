# -*- coding: utf-8 -*-

from odoo import models,fields
class Customer(models.Model):
    
    _inherit = "res.partner"
    product_list_id = fields.Many2one(comodel_name='product.list', string='Customers')

class ProductListsTemplate(models.Model):
    _name = "product.list"
    _description="Template for a product list"

    name = fields.Char(string="Title",required = True)
    description = fields.Text(string = "Description")
    product_list = fields.Many2many(string="Product List",comodel_name="product.product")
    customers_id = fields.One2many(string="Customers that use the list",comodel_name="res.partner", inverse_name="product_list_id")
    #creating field to keep track of product list
    

    