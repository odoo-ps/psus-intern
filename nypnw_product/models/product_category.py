from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def _default_sequence_id(self):
        # This is loaded before XML, so we have to create inline
        out = self.env['ir.sequence'].search(
            [('code', '=', 'nypnw_default_seq')])
        if not out:
            out = self.env['ir.sequence'].create({
                'code': 'nypnw_default_seq',
                'name': 'NY P&W Default Sequence',
                'prefix': 'NYPNW-',
                'padding': 8,
            })
        return out

    sequence_id = fields.Many2one('ir.sequence',
                                  string='Internal Sequence',
                                  required=True,
                                  default=_default_sequence_id)

    def next_name(self):
        return self.sequence_id.next_by_id()
