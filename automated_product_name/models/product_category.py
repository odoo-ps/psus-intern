from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = "product.category"

    sequence_id = fields.Many2one(
        comodel_name='ir.sequence', compute='_compute_sequence', required=True, store=True)
    sequence_number = fields.Char(string='Sequence Number')
    gender = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino'), (
        'indefinido', 'Indefinido')], 'Gender', copy=False, default='indefinido')

    @api.depends('name')
    def _compute_sequence(self):
        ir_sequence_ref = self.env['ir.sequence']
        for category in self:
            if category.name and category.parent_id:
                prefix = category.name[0]+category.parent_id.name[0] + \
                    str.upper(category.gender[0])
                category.sequence_number = ir_sequence_ref.next_by_code(
                    prefix)
                if not category.sequence_number:
                    category.sequence_number = ir_sequence_ref.create({
                        'name': 'Category Sequence',
                        'code': prefix,
                        'prefix': prefix,
                        'padding': 5,
                        'number_increment': 1,
                        'implementation': 'standard',
                    }).next_by_code(prefix)

                category.sequence_id = ir_sequence_ref.search(
                    [('code', '=', prefix)])
                print(category.sequence_number)
                print(category.sequence_id)
