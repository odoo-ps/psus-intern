#-*- coding: uft-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class ProductTemplate(models.Model):
    _inherit='product.template'
    
    pair_per_case=fields.Integer(string="Pair Per Case")
    
    price_per_pair=fields.Float(string="Price Per Pair",default=1)
    
    sales_price=fields.Float(string="Sales Price", 
                             compute="_compute_sales_price",
                             inverse="_inverse_compute_sales_price")
    
    @api.depends("pair_per_case","price_per_pair")
    def _compute_sales_price(self):
        for rec in self:
            if rec.pair_per_case<0 or rec.price_per_pair<0:
               raise UserError("The number can not be negtive!") 
            if rec.pair_per_case and rec.price_per_pair:
               rec.sales_price=rec.pair_per_case*rec.price_per_pair
               
    @api.depends("sales_price")
    def _inverse_compute_sales_price(self):
        for rec in self:
            if rec.pair_per_case==0:
              raise ValidationError('The Pair Per Case can not be zero')
            else:
              rec.price_per_pair=rec.sales_price/rec.pair_per_case 
          
