# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_num_prefix = fields.Selection(
        string='Job Number Prefix',
        selection=[
            ('example1-', 'example1-'),
            ('example2-', 'example2-')
        ])
    job_num_suffix = fields.Selection(
        string='Job Number Suffix',
        selection=[
            ('-sample1', '-sample1'),
            ('-sample2', '-sample2')
        ])
    job_num_sequence = fields.Many2one(comodel_name='ir.sequence', string='Job Number Sequence')

    job_number = fields.Char(string='Job Number', required=True)
    plant_code = fields.Char(string='Plant Code', readonly=True)

    @api.onchange('job_num_prefix', 'job_num_suffix', 'job_num_sequence')
    def _onchange_job_number(self):
        new_job_number = ''

        if self.job_num_prefix:
            new_job_number += self.job_num_prefix

        if self.job_num_sequence:
            new_job_number += self.job_num_sequence.next_by_id()
        else:
            # don't change the job number if there is no sequence selected
            return
        
        if self.job_num_suffix:
            new_job_number += self.job_num_suffix

        self.job_number = new_job_number

    def action_confirm(self):
        super().action_confirm()
        self.plant_code = self.partner_id.commercial_partner_id.next_plant_code()
