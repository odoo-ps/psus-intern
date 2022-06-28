# *-* coding: utf-8 *-*
from odoo import models,fields,api


class Product(models.Model):
    _inherit = "product.template"
    
    lot_number_prefix = fields.Char(string="Lot number prefix", help="Prefix for the lot number")
    
    #lot_number_counter = fields.Integer(string="Lot number counter", help="Counter for the lot number")
    
    