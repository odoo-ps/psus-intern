from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_number = fields.Char(
        string='Job Number', required=True, readonly=True)
    prefix = fields.Selection(
        [('j01', 'J01'), ('j02', 'j02'), ('j03', 'J03'), ('j04', 'J04')],
        string='Prefix',
        required=True)
    sufix = fields.Selection(
        [('-01', '-01'), ('-02', '-02'), ('-03', '-03'), ('-04', '-04')],
        string='Sufix',
        required=True)

    @api.onchange('prefix', 'sufix')
    def _compute_job_number(self):
        if(self.prefix and self.sufix):
            sequence = self.env['ir.sequence'].search(
                [('code', '=', self.prefix + self.sufix)])
            if sequence:
                self.write(
                    {'job_number': (sequence.get_next_char(sequence.number_next_actual))})
            else:
                self.env['ir.sequence'].create({
                    'name': 'Secuence for Lot Number',
                    'code': self.prefix + self.sufix,
                    'prefix': self.prefix,
                    'suffix': self.sufix,
                    'padding': 5,
                    'implementation': 'standard',
                    'number_next': 13500,
                    "number_increment": 1,
                    "active": True,
                })
                sequence = self.env['ir.sequence'].search(
                    [('code', '=', self.prefix + self.sufix)])
                self.write(
                    {'job_number': (sequence.get_next_char(sequence.number_next_actual))})
        else:
            self.write({'job_number': False})

    @api.model
    def create(self, vals):
        vals['job_number'] = self.env['ir.sequence'].next_by_code(
            vals['prefix'] + vals['sufix'])
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        if vals.get('prefix') or vals.get('sufix'):
            if vals.get('prefix'):
                prefix = vals['prefix']
            else:
                prefix = self.prefix
            if vals.get('sufix'):
                sufix = vals['sufix']
            else:
                sufix = self.sufix
            vals['job_number'] = self.env['ir.sequence'].next_by_code(
                prefix + sufix)
        print(vals)
        return super().write(vals)
        
    def action_confirm(self):
        res = super().action_confirm()
        if not (self.partner_id.plant_code):
            self.partner_id._get_plant_code()
        return res
