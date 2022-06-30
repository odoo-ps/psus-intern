# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import re


class SaleOrder(models.Model):
    _inherit = "sale.order"

    job_number = fields.Char(compute="_compute_job_number")
    job_prefix = fields.Selection(
        required=True, default='a',
        selection=[('a', 'A'), ('b', 'B'), ('c', 'C')])
    job_sequence = fields.Char(default=lambda self: _('13500'),
                               readonly=True, store=True)

    plant_code = fields.Char(compute="_compute_plant_code")
    plant_prefix = fields.Char(related="company_id.name")
    plant_sequence = fields.Char(default=lambda self: _('00101'),
                                 readonly=True, store=True)

    @api.depends('job_prefix', 'job_sequence')
    def _compute_job_number(self):
        self.job_number = self.job_prefix.upper() + self.job_sequence

    @api.depends('plant_prefix', 'plant_sequence')
    def _compute_plant_code(self):
        prefix = (re.sub('[^A-Za-z]+', '', self.plant_prefix))[:3]
        sequence = self.plant_sequence[:3] \
            + "-" + self.plant_sequence[3:]
        self.plant_code = prefix.upper() + sequence

    # override create method to set sequences at creation
    @api.model
    def create(self, vals):
        if vals.get('job_sequence', _('13500')) == _('13500'):
            vals['job_sequence'] = \
                self.env['ir.sequence'].next_by_code('sale.order.job.seq') \
                or _('13500')
        if vals.get('plant_sequence', _('00101')) == _('00101'):
            vals['plant_sequence'] = \
                self.env['ir.sequence'].next_by_code('sale.order.plant.seq') \
                or _('00101')
        res = super(SaleOrder, self).create(vals)
        return res
