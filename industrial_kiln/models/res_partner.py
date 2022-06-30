import re

from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = 'res.partner'

    plant_code = fields.Char(string='Plant Code',
                             compute='_compute_plant_code')

    has_confirmed_SO = fields.Boolean(string='Has a confirmed SO.')

    plant_prefix = fields.Char(string='Plant Code Prefix')

    plant_code_sequence_number = fields.Char(string="Sequence for plant code")

    @api.depends('has_confirmed_SO')
    def _compute_plant_code(self):
        for partner in self:
            if not partner.plant_code and partner.has_confirmed_SO:
                partner.plant_code = partner.plant_prefix + partner.plant_code_sequence_number
            else:
                partner.plant_code = partner.plant_code

    @api.model
    def create(self, vals_list):
        partners = super(Partner, self).create(vals_list)
        return partners

    @api.model
    def _create_plant_code_sequence(self, plant_prefix):
        IrSequence = self.env['ir.sequence']
        if IrSequence.search([('code', '=', plant_prefix)]):
            return
        return IrSequence.sudo().create({
            'name': _("Plant Code Sequence {}".format(plant_prefix)),
            'code': plant_prefix,
            'prefix': plant_prefix,
            'number_next': 101,
            'use_date_range': False,
            'padding': 5
        })

    def prepare_plant_code_data(self):
        if self.is_company:
            name = self.name
        else:
            if self.parent_id:
                name = self.parent_id.name
            else:
                name = self.name
        name = re.sub('[^A-Za-z0-9]+', '', name)
        if len(name) >= 3:
            plant_prefix = name.upper()[0:3]
        else:
            plant_prefix = name
        self._create_plant_code_sequence(plant_prefix)
        sequence_number = str(
            self.env['ir.sequence'].next_by_code(plant_prefix))
        self.plant_prefix = plant_prefix
        self.plant_code_sequence_number = sequence_number[3:6] + \
            '-' + sequence_number[6:]
