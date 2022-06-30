import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):

    _inherit = 'res.partner'

    has_confirmed_SO = fields.Boolean(string='Has a confirmed SO.')
    plant_code = fields.Char(string='Plant Code',
                             compute='_compute_plant_code')
    plant_prefix = fields.Char(string='Plant Prefix')

    @api.depends('has_confirmed_SO')
    def _compute_plant_code(self):
        for partner in self:
            if partner.has_confirmed_SO and not partner.plant_code:
                sequence = self.env['ir.sequence'].create({
                    'name': 'Secuence for Lot Number',
                    'code': partner.plant_prefix,
                    'prefix': partner.plant_prefix,
                    'padding': 5,
                    'implementation': 'standard',
                    'number_next': 101,
                    "number_increment": 1,
                    "active": True,
                }).next_by_code(partner.plant_prefix)
                sequence = str(sequence)
                partner.plant_code = sequence[0:6] + '-' + sequence[6:]
            else:
                partner.plant_code = False

    def prepare_plant_prefix(self):
        if self.is_company:
            name = self.name
        else:
            if self.parent_id:
                name = self.parent_id.name
            else:
                name = self.name
        name = re.sub('[^A-Za-z0-9]+', '', name)
        if len(name) >= 3:
            self.plant_prefix = name.upper()[0:3]
        else:
            self.plant_prefix = name
