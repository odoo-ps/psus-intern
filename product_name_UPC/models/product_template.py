from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    name = fields.Char(index=True, required=True, translate=True,
                       default=lambda self: _('New'), readonly=True)

    product_gender = fields.Selection(
        [('M', 'Male'), ('F', 'Female'), ('U', "Unisex"), ('O', 'Other')], default='O', requred=True)

    barcode = fields.Char('Barcode', compute='_compute_barcode',
                          inverse='_set_barcode', search='_search_barcode', readonly=True)

    def create_sequence(self, code, category=None):
        IrSequence = self.env['ir.sequence']
        if not IrSequence.search([('code', '=', code)]):
            prefix = str(code) + '-'
            sequence = IrSequence.create({
                'name': code,
                'code': code,
                'prefix': prefix,
                'number_next': 1,
                'padding': 7,
            })
            if category:
                category.category_sequence_id = sequence
        return self.env['ir.sequence'].next_by_code(
            str(code))

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', _('New')) == _('New'):
            category = self.env['product.category'].search(
                [('id', '=', vals_list.get('categ_id'))])
            vals_list['name'] = self.create_sequence(category.name, category)
            vals_list['barcode'] = self.create_sequence(
                vals_list['product_gender'])
            return super(ProductTemplate, self).create(vals_list)

    def write(self, vals_list):
        category = self.env['product.category'].search(
            [('id', '=', vals_list.get('categ_id'))])
        if 'categ_id' in vals_list.keys():
            vals_list['name'] = self.create_sequence(category.name, category)
        if 'product_gender' in vals_list.keys():
            vals_list['barcode'] = self.create_sequence(
                vals_list['product_gender'])
        return super(ProductTemplate, self).write(vals_list)
