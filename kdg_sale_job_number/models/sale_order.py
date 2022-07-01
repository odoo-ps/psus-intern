# -*- coding: utf-8 -*-

from sre_constants import BRANCH
from odoo import fields,api,models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_number = fields.Text(string="Job Number", store=True, copy=False)
    job_number_internal = fields.Text(string="Internal Sequence", copy=False)
    job_prefix = fields.Selection(string="Job Prefix", selection=[("Pre-","Pre-"),("Re-","Re-"),("Semi-","Semi-")] )
    job_suffix = fields.Selection(string="Job Suffix", selection=[("-ion","-ion"),('-ice',"-ice"),("-fire","-fire")] )
        
    @api.model
    def create(self, vals):
        sequence_num = self.env['ir.sequence'].next_by_code('job.number')
        vals['job_number_internal'] = sequence_num
        vals['job_number'] = (vals['job_prefix'] if vals['job_prefix'] else '') + sequence_num + (vals['job_suffix'] if vals['job_suffix'] else '')
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        if 'job_prefix' in vals or 'job_suffix' in vals:
            for sale_order in self:
                prefix = (vals['job_prefix'] if 'job_prefix' in vals else sale_order.job_prefix)
                suffix = (vals['job_suffix'] if 'job_suffix' in vals else sale_order.job_suffix)

                if not prefix:
                    prefix = ''
                
                if not suffix:
                    suffix = ''

                vals['job_number'] = prefix + sale_order.job_number_internal + suffix
        return super(SaleOrder, self).write(vals)
    
    @api.onchange('job_suffix','job_prefix')
    def _onchange_affix(self):
        if not self._origin.id:
            seq = self.env['ir.sequence'].search([('code','=','job.number')])
            self.job_number = (self.job_prefix if self.job_prefix else '') + seq.get_next_char(seq.number_next_actual) + (self.job_suffix if self.job_suffix else '')
        else:
            self.job_number = (self.job_prefix if self.job_prefix else '') + self.job_number_internal + (self.job_suffix if self.job_suffix else '')
      
    def action_confirm(self):
        if not self.partner_id.plant_code:
            if self.partner_id.parent_id.is_company:
                partner_code = ''.join(filter(str.isalnum, self.partner_id.parent_id.name))[:3]
            else:
                partner_code = ''.join(filter(str.isalnum, self.partner_id.name))[:3]

            base_seq = self.env['ir.sequence'].search([('code','=','plant.code')])
            sub_seq = self.env['ir.sequence'].search([('code','=','plant.code.sub')])
            
            if sub_seq.number_next_actual < 99:
                plant_code = partner_code + base_seq.get_next_char(base_seq.number_next_actual) + '-' + sub_seq._next()
            else:        
                sub_seq.update({'number_next': 1})
                plant_code = partner_code + base_seq._next() + '-' + sub_seq.get_next_char(sub_seq.number_next_actual)
            
            self.partner_id.update({'plant_code': plant_code})
        return super(SaleOrder, self).action_confirm()