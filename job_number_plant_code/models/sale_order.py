# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    job_number = fields.Char()
    job_prefix = fields.Selection(
        string="Prefix",
        selection=[('a', 'A'), ('b', 'B')])
    job_sequence = fields.Char(default=lambda self: _('13500'),
                               readonly=True)

    plant_code = fields.Char()
    plant_sequence = fields.Char(default=lambda self: _('00101'),
                                 readonly=True)

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
