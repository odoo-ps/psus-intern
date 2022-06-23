# -*- coding: utf-8 -*-
from odoo import models,fields,api

class ProductTemplate(models.Model):
    _inherit='product.template'
    pairs_per_case = fields.Integer(
        string='Pairs per case',default=0)

    price_per_pair = fields.Monetary(
        string = 'Price per pair',default=0.0)
        
    list_price = fields.Float(
        string='Sales Price',
        digits='Product Price',
        help="Price at which the product is sold to customers.",
        compute='_compute_sales_price',store=True
    )
    @api.depends('pairs_per_case','price_per_pair')
    def _compute_sales_price(self):
            
        self.list_price = self.pairs_per_case*self.price_per_pair
        