from odoo import fields,models

class IrSequence(models.Model):
  _inherit = 'ir.sequence'

  product_category = fields.One2many(
    comodel_name='product.category',
    inverse_name='sequence'
  )
