# -*- coding: utf-8 -*-

from email.policy import default
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(required=False)

    gender = fields.Selection(string='gender',
                            selection=[('one', 'One'),
                                       ('two', 'Two'),
                                       ('three', 'Three')],
                            default='one')

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val['barcode'] = self.env['ir.sequence'].next_by_code('product.barcode')
            if not val['name']:
                val['name'] = self.env['ir.sequence'].next_by_code('product.template')
            else:
                products = self.env['product.product'].search_read([('name', '=', val['name'])])
                if len(products) > 0:
                    raise ValidationError(_("Product name already existed"))
        return super(ProductTemplate, self).create(vals_list)
    
    def write(self, vals):
        if "categ_id" in vals:
            vals["name"] = self.env['ir.sequence'].next_by_code('product.template')
        return super(ProductTemplate, self).write(vals)
