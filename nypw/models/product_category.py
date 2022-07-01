# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):

    _inherit = 'product.category'

    cat_seq = fields.Many2one(comodel_name='ir.sequence', string='Cat Seq')

    @api.depends('name')
    def _compute_sequence(self):
        for rec in self:
            if not rec.cat_seq:
                vals = {
                    'name': rec.name,
                    'code': rec.name,
                    'implementation': 'standard',
                    'active': True,
                    'prefix': rec.name,
                    'number_next': 1,
                    'number_increment': 1,
                    'padding': 5,
                }
                rec.cat_seq = self.env['ir.sequence'].create(vals)