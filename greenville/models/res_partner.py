from odoo import fields, models

class ResPartner(models.Model):
  _inherit='res.partner'

  product_lists = fields.Many2many(
    string='Product List',
    comodel_name='product.list',
  )
