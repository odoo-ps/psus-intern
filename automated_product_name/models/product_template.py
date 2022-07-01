from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _sql_constraints = [
        ('name_unique', 'unique(name)',
         'You can not have two products with the same name !')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        vals_list[0]['name'] = self._update_name(
            vals_list[0]['categ_id'], vals_list[0]['name'])
        gender_sequence = (self.generate_sequence(
            {'name': 'Gender Sequence', 'code': vals_list[0]['categ_id'], 'prefix': vals_list[0]['categ_id'], 'padding': 5, 'number_increment': 1, 'implementation': 'standard'}))
        vals_list[0]['barcode'] = f"{gender_sequence}-{vals_list[0]['name']}"
        templates = super().create(vals_list)

        return templates

    def write(self, vals):
        if 'categ_id' in vals:
            vals['name'] = self._update_name(vals['categ_id'], self.name)
            vals['barcode'] = f"{self.barcode.split('-')[0]}-{vals['name']}"

        return super().write(vals)

    def _update_name(self, categ_id, name):
        categ_ref = self.env['product.category'].search(
            [('id', '=', categ_id)])
        new_name = name or ''
        prefix = str.upper(new_name[0:2] or new_name[0])
        if categ_ref.sequence_number:
            new_name = f"{categ_ref.sequence_id.code}{self.generate_sequence({'name':'Product Sequence','code':prefix,'prefix':prefix,'padding':5,'number_increment':1,'implementation':'standard'})}"
        
        return new_name

    # Generates sequence for product name

    def generate_sequence(self, vals):
        ir_sequence_ref = self.env['ir.sequence']
        sequence_number = ir_sequence_ref.next_by_code(
            vals['prefix'])
        if not sequence_number:
            sequence_number = ir_sequence_ref.create({
                'name': vals['name'],
                'code': vals['code'],
                'prefix': vals['prefix'],
                'padding': vals['padding'],
                'number_increment': vals['number_increment'],
                'implementation': vals['implementation'],
            }).next_by_code(vals['prefix'])

        return sequence_number
