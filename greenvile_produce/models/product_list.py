from odoo import api,fields,_,models


class ProductList(models.Model):
    _name='greenvile.produce.productlist'

    products = fields.Many2many(comodel_name='product.template',relation='product_list_product_template_rel',column1='product_list_id',column2='product_template_id')

    customers = fields.One2many(comodel_name='res.partner',inverse_name="products_to_purchase")
    