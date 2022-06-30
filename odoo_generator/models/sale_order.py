from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    job_number = fields.Text(
        string='Job Number')

    plant_code = fields.Text(string='Plant Code')

    job_prefix = fields.Selection([('101', '101'),
                                   ('201', '201'),
                                   ('301', '301'),
                                   ('401', '401'),
                                   ('401', '401')],
                                  'Job Prefix', copy=False, required=True, default='101',
                                  help="Prefix of the job number.\n")

    job_suffix = fields.Selection([('zac', 'ZAC'),
                                   ('tyr', 'TYR'),
                                   ('hec', 'HEC'),
                                   ('edu', 'EDU'),
                                   ('ale', 'ALE')],
                                  'Job Suffix', copy=False, required=True, default='zac',
                                  help="Suffix of the job number.\n")

    # override the function create of the sale order to generate the job number
    @api.model
    def create(self, vals):
        if vals.get('job_prefix') and vals.get('job_suffix'):
            ir_sequence = self.env['ir.sequence']
            vals['job_number'] = ir_sequence.next_by_code(
                vals['job_prefix'] + vals['job_suffix'])
            if not vals['job_number']:
                vals['job_number'] = ir_sequence.create({
                    'name': 'Job Number',
                    'code': vals['job_prefix'] + vals['job_suffix'],
                    'prefix': vals['job_prefix'],
                    'suffix': vals['job_suffix'],
                    'padding': 5,
                    'number_next': 13500,
                    'number_increment': 1,
                    'implementation': 'standard',
                }).next_by_code(vals['job_prefix'] + vals['job_suffix'])
        return super().create(vals)

     # override the function write of the sale order to generate the job number
    def write(self, vals):
        job_suffix = vals.get('job_suffix') if vals.get(
            'job_suffix') else self.job_suffix
        job_prefix = vals.get('job_prefix') if vals.get(
            'job_prefix') else self.job_prefix
        vals['job_number'] = self.job_number
        if job_prefix and job_suffix:
            ir_sequence = self.env['ir.sequence']
            sequence = ir_sequence.search(
                [('code', '=', job_prefix + job_suffix)])
            if (not vals['job_number'] or not sequence):
                vals['job_number'] = ir_sequence.create({
                    'name': 'Job Number',
                    'code': job_prefix + job_suffix,
                    'prefix': job_prefix,
                    'suffix': job_suffix,
                    'padding': 5,
                    'number_next': 13500,
                    'number_increment': 1,
                    'implementation': 'standard',
                }).next_by_code(job_prefix + job_suffix)
            else:
                vals['job_number'] = sequence.next_by_code(
                    job_prefix + job_suffix)
        return super().write(vals)

    def action_confirm(self):
        res = super().action_confirm()
        if not self.partner_id.has_confirmed_SO:
            self.partner_id.prepare_plant_prefix()
            self.partner_id.has_confirmed_SO = True
        return res
