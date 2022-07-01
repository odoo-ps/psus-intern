from odoo import models,fields

class ProductTemplate(models.Model):
    _inherit='product.template'

    lists = fields.Many2many(comodel_name='greenvile.produce.productlist',relation='product_template_product_list_rel',column1='product_template_id',column2='product_list_id')