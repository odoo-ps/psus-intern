import re

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    plant_code = fields.Char(string='Plant Code',
                             compute='_compute_plant_code',
                             readonly=True,
                             store=True)

    has_confirmed_SO = fields.Boolean(string='Has a confirmed SO.',
                                      compute='_compute_has_confirmed_SO',
                                      default=False)

    plant_prefix = fields.Char(string='Plant Code Prefix')

    def _compute_has_confirmed_SO(self):
        self.ensure_one()
        if not self.has_confirmed_SO:
            if self.env['sale.order'].search([('state', '=', 'sale'), ('partner_id', '=', self.id)]):
                self.has_confirmed_SO = True
                self._compute_plant_code()

    @api.depends('has_confirmed_SO')
    def _compute_plant_code(self):
        if not self.plant_code:
            if self.has_confirmed_SO:
                name = self.name
                name = re.sub('[^A-Za-z0-9]+', '', name)
                self.plant_prefix = name.upper()[0:3]
                self._create_plant_code_sequence()
                sequence_number = str(
                    self.env['ir.sequence'].next_by_code(self.plant_prefix))
                self.plant_code = self.plant_prefix + \
                    sequence_number[3:6] + '-' + sequence_number[6:]
        else:
            self.plant_code = self.plant_code

    @api.model
    def _create_plant_code_sequence(self):
        IrSequence = self.env['ir.sequence']
        if IrSequence.search([('code', '=', self.plant_prefix)]):
            return
        return IrSequence.sudo().create({
            'name': _("Plant Code Sequence {}".format(self.plant_prefix)),
            'code': self.plant_prefix,
            'prefix': self.plant_prefix,
            'number_next': 101,
            'use_date_range': False,
            'padding': 5
        })
