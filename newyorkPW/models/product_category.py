from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit="product.category"

    sequence_code = fields.Many2one('ir.sequence', string='Internal Sequence', inverse_name='product_category_id') 
    gender = fields.Selection([('M', 'Male'),('F', 'Female'),('U',"Undefinded")], default="U")
