# -*- coding:utf-8 -*-


from odoo import models, fields, api


class product_template_inherit_model(models.Model):
    _inherit = 'product.category'

    product_sequence_id = fields.Many2one(
        'product.template', 
        string='Product Sequence',
        compute = 'get_new_sequence_id'
        )

    @api.depends('name')
    def get_new_sequence_id(self):
        for record in self:
            record.product_sequence_id = record.name
    