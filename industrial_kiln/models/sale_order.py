from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    job_number = fields.Text(
        string="Job Number", required=True, default='000000')

    @api.model_create_multi
    def create(self, vals_list):

        vals_list[0] = self._update_job_number(vals_list[0])

        return super().create(vals_list)

    def write(self, values):
        values = self._update_job_number(values)
        result = super().write(values)
        return result

    def _update_job_number(self, vals):

        new_code = (vals.get('x_studio_prefix') or self.x_studio_prefix) + \
            (vals.get('x_studio_suffix') or self.x_studio_suffix)
        vals.update(job_number=(self.generate_sequence(
            {
                'name': 'Job Number',
                'code': new_code,
                'prefix': vals.get('x_studio_prefix') or self.x_studio_prefix,
                'suffix': vals.get('x_studio_suffix') or self.x_studio_suffix,
                'padding': 5,
                'number_increment': 1,
                'number_next': 13500,
                'implementation': 'standard'
            }
        )))
        return vals

    def action_confirm(self):
        res = super().action_confirm()
        if not (self.partner_id.plant_code):
            self.partner_id._get_plant_code()
        return res

    def generate_sequence(self, vals):
        ir_sequence_ref = self.env['ir.sequence']
        sequence_number = ir_sequence_ref.next_by_code(
            vals['code'])
        if not sequence_number:
            sequence_number = ir_sequence_ref.create({
                'name': vals['name'],
                'code': vals['code'],
                'prefix': vals['prefix'],
                'suffix': vals['suffix'],
                'padding': vals['padding'],
                'number_increment': vals['number_increment'],
                'number_next': vals['number_next'],
                'implementation': vals['implementation'],
            }).next_by_code(vals['code'])

        return sequence_number
