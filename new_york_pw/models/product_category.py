from odoo import fields,models

class ProductCategory(models.Model):
  _inherit = 'product.category'

  sequence = fields.Many2one(
    comodel_name='ir.sequence',
    required=True
  )

  gender = fields.Selection(
    string='Gender',
    selection=[
      ('M','Male'),
      ('F','Female')
    ],
    required=True
  )
