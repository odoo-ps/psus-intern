from odoo import fields,models,api

class ProductCategory(models.Model):
    _inherit="product.category"
    
    category_seq_id = fields.Many2one(
        string='Category Sequence',
        comodel_name='ir.sequence',
        ondelete='restrict',
        compute='_add_sequence_model',
        store=True
    )
    @api.depends('name')
    def _add_sequence_model(self):
        
        for record in self.env['product.category'].search([]):
            print(record.name)
            print(not record.category_seq_id)
            print(record.category_seq_id)
            if not record.category_seq_id:
                sequence_map = {
                    "name" : record.name,
                    "code":  record.complete_name,
                    "prefix":record.name,
                    "number_increment":1,
                    "number_next":300000,
                    "implementation":"standard"
                }
                record.category_seq_id = self.env['ir.sequence'].create(sequence_map)
    