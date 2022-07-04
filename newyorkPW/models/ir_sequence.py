from odoo import models, fields, api, _



class irSequence(models.Model):
    _inherit = "ir.sequence"
    
    product_category_id = fields.One2many('product.category', string='Product Category', inverse_name='sequence_code')
    
    
    