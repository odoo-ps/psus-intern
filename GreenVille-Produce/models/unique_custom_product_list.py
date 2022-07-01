# -*- coding:utf-8 -*-


from odoo import models, fields, api


class unique_custom_product_list(models.Model):
    _name = 'greenville.product'
    _description = "List of products specific for a customer"

    name = fields.Char(string = 'Title', required = True )

    product_lists = fields.Many2many('product.template', string="Product List")

    customer_using_product_list = fields.One2many( 'res.partner', 'product_list_to_customers' , string="Customer List" )