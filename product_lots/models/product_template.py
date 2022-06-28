# *-* coding: utf-8 *-*
from odoo import fields,models,api

class ProductTemplate(models.Model):
    _inherit="product.template"
    
    lot_number_prefix = fields.Char(string="Lot Number Prefix")
    
    
    