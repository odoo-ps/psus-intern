from odoo import fields, models


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'
    
    name = fields.Char(string='Product List Name')
    
    product_ids = fields.Many2many(comodel_name='product.template',
        string='Products in this list')
    
    customer_ids = fields.One2many(comodel_name='res.partner',
        inverse_name='product_list_id',
        string='Customers That Use This list')
