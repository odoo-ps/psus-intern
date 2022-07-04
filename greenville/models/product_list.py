from odoo import fields, models

class ProductList(models.Model):
  _name = 'product.list'
  _description = 'A product list for show to the customer those that he will buy'

  name = fields.Char(
    string='List Name', 
    required=True
  )

  products = fields.Many2many(
    string='Products',
    comodel_name='product.template'
  )

  customer = fields.Many2many(
    string='Customer',
    comodel_name='res.partner',
  )
