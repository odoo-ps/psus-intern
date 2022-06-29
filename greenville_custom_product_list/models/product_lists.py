# -*- coding: utf-8 -*-
from odoo import models,fields,api


class ProductListsTemplate(models.Model):
    
    _name='product.list'
    _description='This is a list of products which can be assigned to a customer'
    
    
    name = fields.Char(
        string='List Name',
        required= True
    )
    description = fields.Text(string="Description")

    product_list_id = fields.Many2many(
        string='Products in List',
        comodel_name='product.template'
    )
    product_customer_id = fields.One2many(
        string='Customer List',
        comodel_name='res.partner',
        inverse_name='product_list_name_id'
        
    )
    
    
    
