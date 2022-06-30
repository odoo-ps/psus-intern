# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):

    _inherit = 'product.category'

    cat_seq = fields.Many2one(comodel_name='ir.sequence', string='Cat Seq', compute='_compute_sequence', store=True)

    @api.depends('name')
    def _compute_sequence(self):
        if not self.cat_seq:
            vals = {
                'name': self.name,
                'code': self.name,
                'implementation': 'standard',
                'active': True,
                'prefix': self.name,
                'number_next': 1,
                'number_increment': 1,
                'padding': 5,
            }
            self.cat_seq = self.env['ir.sequence'].create(vals)