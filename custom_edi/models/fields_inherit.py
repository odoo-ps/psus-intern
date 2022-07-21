
from odoo import models, fields, api

class ModelField(models.Model):
    _inherit = 'ir.model.fields'

    def view_subfields(self):
        ctx = self.env.context.copy()
        # Update the field_path by adding the selected field and adding '.' as a separator
        if 'field_path' in ctx:
            ctx['field_path'] += '.' + self.name
        else:
            ctx['field_path'] = self.name

        return {
            'name': self.field_description,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'ir.model.fields',
            'domain': [('model', '=', self.relation)],
            'view_mode': 'tree',
            'target': 'new',
            'res_id': self.id,
            'context': ctx
        }

    def create_edi_tag(self):
        ctx = self.env.context.copy()
        # Update the field_path by adding the selected field and adding '.' as a separator
        if 'field_path' in ctx:
            ctx['field_path'] += '.' + self.name
        else:
            ctx['field_path'] = self.name

        ctx['field_id'] = self.id
        # Create a dictionary with relevant values to call the create() method and make a new EDI Tag record
        vals = {
            'field_path': ctx['field_path'],
            'field_id': ctx['field_id'],
        }
        # If the EDI Tag to make is a child of another, update the parent ID, and remove the parent's field_path from
        # the tag to make
        if 'parent_edi_tag' in self._context:
            vals['parent_tag_id'] = self._context['parent_edi_tag']
            # Search for the parent EDI Tag object
            parent_edi_tag = self.env['edi.tag'].search([('id', '=', vals['parent_tag_id'])])
            parent_path = parent_edi_tag.field_path + '.'
            vals['field_path'] = vals['field_path'].replace(parent_path, '')
            ctx['field_path'] = vals['field_path']
        else:
            # If the EDI Tag to make has no parent, assign the custom mapping
            vals['custom_mapping'] = self._context['parent_mapping']

        self.env['edi.tag'].create(vals)
        # Search for the EDI Tag object just created and open the form view corresponding to it
        edi_tag = self.env['edi.tag'].search([('field_path', '=', vals['field_path'])])
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'edi.tag',
            'res_id': edi_tag.id,
            'view_mode': 'form',
            'target': 'new',
            'flags': {'action_buttons': False},
            'context': ctx,
        }