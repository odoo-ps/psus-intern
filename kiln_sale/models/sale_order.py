import re
from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_number = fields.Char(string='Job Number',
                             compute='_compute_job_number',
                             inverse='_set_job_number',
                             store=True)
    sequence_id = fields.Many2one('ir.sequence',
                                  string='Job Number Sequence',
                                  compute='_compute_sequence_id',
                                  inverse='_set_sequence_id',
                                  store=True)

    @api.depends('sequence_id')
    def _compute_job_number(self):
        for record in self:
            if record.sequence_id and not record.job_number:
                record.job_number = record.sequence_id.next_by_id()

    @api.depends('x_studio_prefix', 'x_studio_suffix')
    def _compute_sequence_id(self):
        for record in self:
            if record.x_studio_prefix or record.x_studio_suffix:
                code = 'sale.order.%s_%s' % (
                    record.x_studio_prefix, record.x_studio_suffix)
                seq = self.env['ir.sequence'].search([('code', '=', code)])
                if not seq:
                    seq = self.env['ir.sequence'].create({
                        'code': code,
                        'name': _('Sale Order %s-%s', record.x_studio_prefix, record.x_studio_suffix),
                        'number_next': 13500,
                        'prefix': record.x_studio_prefix or '',
                        'suffix': record.x_studio_suffix or '',
                    })
                record.sequence_id = seq

    def _set_sequence_id(self):
        for record in self:
            if record.sequence_id:
                record.x_studio_prefix = record.sequence_id.prefix
                record.x_studio_suffix = record.sequence_id.suffix

    def _set_job_number(self):
        for record in self:
            if not record.job_number:
                # User forced re-evaluation of job number
                record.job_number = record.sequence_id.next_by_id()

    def action_confirm(self):
        res = super().action_confirm()
        if not self.partner_id.plant_no:
            company_name = self.partner_id.parent_id and self.partner_id.parent_id.name or self.partner_id.name
            company_name = (
                re.compile('[^a-zA-Z0-9]')
                .sub('', company_name)
                .rjust(3, '_')[:3]
                .upper()
            )
            plant_no = self.env['ir.sequence'].next_by_code(company_name)
            if not plant_no:
                plant_no = self.env['ir.sequence'].create({
                    'code': company_name,
                    'name': _('%s Sequence', company_name),
                    'padding': 5,
                    'prefix': company_name,
                }).next_by_id()
            # "CMPXXXXX" -> "CMPXXX-XX"
            plant_no = plant_no[:6] + '-' + plant_no[6:]
            self.partner_id.plant_no = plant_no
        return res
