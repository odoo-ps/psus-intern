# -*- coding:utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError


class ProductLists(models.Model):
    _name = 'custom.productlists'


    name= fields.Char('Product List Item')   
    product_list_id= fields.Many2many(comodel_name='product.template',
                                   relation='product_list_custom_rel',
                                   string="Product Template",
                                   store=True
                                   )
    tag_ids = fields.One2many(comodel_name='custom.producttags',
                              inverse_name='name',
                              string="Tags")
    customer_list_ids=fields.One2many(comodel_name='res.partner', 
                                      inverse_name='product_list_ids',
                                      string="Customer Using List",
                                      store=True
                                     )
    
  
class ProductTags(models.Model):
    _name='custom.producttags'
    
    name=fields.Char('tag name')
    