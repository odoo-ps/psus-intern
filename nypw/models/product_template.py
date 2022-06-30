# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    name = fields.Char(string='Name', store=True)

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
        vals['name'] = self.env['ir.sequence'].next_by_code(this_cat.cat_seq.code)
        result = super(ProductTemplate, self).create(vals)
        return result

    def write(self, vals):
        if 'categ_id' in vals.keys():
            this_cat = self.env['product.category'].search([('id', '=', vals['categ_id'])])
            self['name'] = self.env['ir.sequence'].next_by_code(this_cat.cat_seq.code)
        result = super(ProductTemplate, self).write(vals)
        return result