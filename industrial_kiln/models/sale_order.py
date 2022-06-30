from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_number_prefix = fields.Selection(
        [('01', '01'), ('02', '02'), ('03', '03')], copy=False, required=True)

    job_number_sufix = fields.Selection(
        [('01', '01'), ('02', '02'), ('03', '03')], copy=False, required=True)

    job_sequence = fields.Integer(string="Job Sequence",
                                  compute='_compute_job_sequence',
                                  store=True)

    job_number = fields.Char(
        compute='_compute_job_number', string='Job Number')

    @api.depends('job_number_prefix')
    def _compute_job_sequence(self):
        for sale_order in self:
            if sale_order.job_sequence == 0:
                if sale_order.name != _('New'):
                    sale_order.job_sequence = self.env['ir.sequence'].next_by_code(
                        'sale.order.job.number') or 23500
                else:
                    sale_order.job_sequence = 0
            else:
                sale_order.job_sequence = sale_order.job_sequence

    @api.depends('job_number_prefix', 'job_number_sufix', 'job_sequence')
    def _compute_job_number(self):
        for sale_order in self:
            sale_order.job_number = str(sale_order.job_number_prefix) + str(
                sale_order.job_sequence) + str(sale_order.job_number_sufix)

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        self._create_job_number_sequence()
        return res

    @api.model
    def _create_job_number_sequence(self):
        IrSequence = self.env['ir.sequence']
        if IrSequence.search([('code', '=', 'sale.order.job.number')]):
            return
        return IrSequence.sudo().create({
            'name': _("Job Number Sequence"),
            'code': 'sale.order.job.number',
            'number_next': 13500,
            'number_increment': 1,
            'use_date_range': False,
        })

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if not self.partner_id.has_confirmed_SO:
            self.partner_id.prepare_plant_code_data()
            self.partner_id.has_confirmed_SO = True
        return res
