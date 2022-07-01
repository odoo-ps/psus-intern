# -*- coding:utf-8 -*-


from odoo import models, fields, api,_


class product_template_inherit_model(models.Model):
    _inherit = 'product.template'

    name = fields.Char(index=True, required=True, translate=True, default=lambda self: _('New'))

    product_gender = fields.Selection(string='Product Gender', selection=[
                                                        ('producttype1', 'Product Type 1'),
                                                        ('producttype2', 'Product Type 2'),
                                                        ('producttype3', 'Product Type 3'),
                                                        ('producttype4', 'Product Type 4'),
                                                        ('producttype5', 'Product Type 5')
                                                       ],
                             copy = False
                            )

    unique_product_code = fields.Char( string = 'UPC')

    @api.onchange('product_gender')
    def generate_upc(self):
        if self.product_gender == 'producttype1':
            self.unique_product_code = 'PT1' + self.env['ir.sequence'].next_by_code('product.template.upc.generator.pt.one')
        elif self.product_gender == 'producttype2':
            self.unique_product_code = 'PT2' + self.env['ir.sequence'].next_by_code('product.template.upc.generator.pt.two')
        elif self.product_gender == 'producttype3':
            self.unique_product_code = 'PT3' + self.env['ir.sequence'].next_by_code('product.template.upc.generator.pt.three')
        elif self.product_gender == 'producttype4':
            self.unique_product_code = 'PT4' + self.env['ir.sequence'].next_by_code('product.template.upc.generator.pt.four')
        elif self.product_gender == 'producttype5':
            self.unique_product_code = 'PT5' + self.env['ir.sequence'].next_by_code('product.template.upc.generator.pt.five')
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            category_found = self.env['product.category'].search([('id', '=', vals['categ_id'])], limit=1 )
            sequence_prefix = category_found.product_sequence_id.id

            vals['name'] = sequence_prefix + self.env['ir.sequence'].next_by_code('product.template')
        return super(product_template_inherit_model, self).create(vals)
    
    @api.model
    def write(self, vals):
        if 'name' in vals and vals.get('name', _('New')) == _('New'):
            category_found = self.env['product.category'].search([('id', '=', vals['categ_id'])], limit=1 )
            sequence_prefix = category_found.product_sequence_id.id
            vals['name'] = sequence_prefix + self.env['ir.sequence'].next_by_code('product.template')
        return super(product_template_inherit_model, self).write(vals)