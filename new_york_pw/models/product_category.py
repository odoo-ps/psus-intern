from odoo import fields, models


class ProductCategory(models.Model):
  _inherit = 'product.category'

  def _default_sequence_id(self):
    res = self.env['ir.sequence'].search([('code', '=', 'nypw_seq')])
    if not res:
      res = self.env['ir.sequence'].create({
        'code': 'nypw_seq',
        'name': 'NY P&W Sequence',
        'prefix': 'NYPW',
        'padding': 6,
    })
    return res

  sequence_id = fields.Many2one('ir.sequence',
                string='Internal Sequence',
                required=True,
                default=_default_sequence_id)
