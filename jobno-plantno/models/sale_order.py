# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_prefix = fields.Selection(string='Job Prefix', selection=[('01', '01'), ('02', '02')])
    job_suffix = fields.Selection(string='Job Suffix', selection=[('0b', '0b'), ('0a', '0a')])
    job_number = fields.Char(string='Job Number', compute='_compute_job_number', store=True)

    company_prefix = fields.Char(string='Company Prefix', compute='_compute_company_prefix')
    plant_number = fields.Char(string='Plant Number', compute='_compute_plant_number', store=True)

    @api.depends('job_prefix', 'job_suffix')
    def _compute_job_number(self):
        for so in self:
            if not so.job_prefix or not so.job_suffix:
                so.job_number = ''
            else:
                sequence = self.env['ir.sequence'].search([('code', '=', 'job.number.sequence')])
                so.job_number = so.job_prefix + sequence.get_next_char(sequence.number_next_actual) + so.job_suffix

    @api.depends('partner_id')
    def _compute_company_prefix(self):
        for so in self:
            so.company_prefix = ''
            if so.partner_id:
                special_chars = '[ @_!#$%^&*()<>?/\|}{~:]'
                char, char_count = 0, 0
                while char_count < 3:
                    if so.partner_id.name[char] not in special_chars:
                        so.company_prefix += so.partner_id.name[char].upper()
                        char_count += 1
                    char += 1
            else:
                so.company_prefix = ''

    @api.depends('company_prefix')
    def _compute_plant_number(self):
        for so in self:
            if so.company_prefix:
                sequence_plant = self.env['ir.sequence'].search([('code', '=', 'plant.number.sequence')])
                plant_no = sequence_plant.get_next_char(sequence_plant.number_next_actual)
                so.plant_number = so.company_prefix + plant_no[:3] + '-' + plant_no[2:]
            else:
                so.plant_number = ''

    @api.model
    def create(self, vals):
        vals['job_number'] = vals.get('job_prefix') + self.env['ir.sequence'].next_by_code('job.number.sequence') + vals.get('job_suffix')
        self.env['ir.sequence'].next_by_code('plant.number.sequence')
        return super().create(vals)
