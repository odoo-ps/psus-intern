# -*- coding: utf-8 -*-

from odoo import models, fields


class PlantCode(models.Model):
    _name = 'plant.code'

    name = fields.Char(string='Name')
    company_prefix = fields.Char(required=True, string='Company Prefix')
    code_sequence_id = fields.Many2one(comodel_name='ir.sequence', string='Sequence')

    def next_plant_code(self):
        if not self.code_sequence_id:
            self.code_sequence_id = self.env['ir.sequence'].create({
                'name': f'Plant Code: {self.company_prefix}',
                'prefix': self.company_prefix,
                'padding': 5
                })
        next_code = self.code_sequence_id.next_by_id()
        return f'{next_code[:-2]}-{next_code[-2:]}'