# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    name = fields.Char(string='Name', store=True, readonly=True, default=' ')
    gender = fields.Selection(
        string='Product Gender',
        selection=[
            ('gender1', 'Gender 1'),
            ('gender2', 'Gender 2'),
            ('gender3', 'Gender 3'),
            ('gender4', 'Gender 4')
            ],
            default='gender1'
        )
    gender_sequence = fields.Char(string='Product Gender Sequence', required=False, readonly=True)

    @api.model
    def create(self, vals):
        recs = self.env['product.category'].search([])
        for rec in recs:
            if not rec.cat_seq:
                temp_vals = {
                'name': rec.name,
                'code': rec.name,
                'implementation': 'standard',
                'active': True,
                'prefix': rec.name,
                'number_next': 1,
                'number_increment': 1,
                'padding': 5,
                }
                rec.cat_seq = self.env['ir.sequence'].create(temp_vals)
        this_cat = self.env['product.category'].search([('id', '=', vals['categ_id'])])
        vals.update({'name': self.env['ir.sequence'].next_by_code(this_cat.cat_seq.code)})
        gender_sequence = self.env['ir.sequence'].search([('name', '=', self.gender)])
        if not gender_sequence:
            temp1 = {
                'name': vals['gender'],
                'code': vals['gender'],
                'implementation': 'standard',
                'active': True,
                'prefix': vals['gender'],
                'number_next': 1,
                'number_increment': 1,
                'padding': 3,
            }
            temp = self.env['ir.sequence'].create(temp1)
            vals['gender_sequence'] = self.env['ir.sequence'].next_by_code(temp.code)
        else:
            self.gender_sequence = self.env['ir.sequence'].next_by_code(gender_sequence.code)
        return super(ProductTemplate, self).create(vals)

    def write(self, vals):
        if 'categ_id' in vals.keys():
            this_cat = self.env['product.category'].search([('id', '=', vals['categ_id'])])
            self['name'] = self.env['ir.sequence'].next_by_code(this_cat.cat_seq.code)
        if 'gender' in vals.keys():
            gender_sequence = self.env['ir.sequence'].search([('name', '=', vals['gender'])])
            if not gender_sequence:
                temp1 = {
                    'name': vals['gender'],
                    'code': vals['gender'],
                    'implementation': 'standard',
                    'active': True,
                    'prefix': vals['gender'],
                    'number_next': 1,
                    'number_increment': 1,
                    'padding': 3,
                }
                temp = self.env['ir.sequence'].create(temp1)
                self['gender_sequence'] = self.env['ir.sequence'].next_by_code(temp.code)
            else:
                self.gender_sequence = self.env['ir.sequence'].next_by_code(gender_sequence.code)
        result = super(ProductTemplate, self).write(vals)
        return result