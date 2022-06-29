from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_number_prefix = fields.Selection(
        [('01', '01'), ('02', '02'), ('03', '03')], copy=False, default='01')

    job_number_sufix = fields.Selection(
        [('01', '01'), ('02', '02'), ('03', '03')], copy=False, default='01')

    job_sequence = fields.Integer(string="Job Sequence")

    job_number = fields.Char(
        compute='_compute_job_number', string='Job Number')

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

    @api.model
    def create(self, vals):
        self._create_job_number_sequence()
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'sale.order', sequence_date=seq_date) or _('New')
        vals['job_sequence'] = self.env['ir.sequence'].next_by_code(
            'sale.order.job.number') or 23500

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault(
                'partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault(
                'partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault(
                'pricelist_id', partner.property_product_pricelist.id)
        result = super(SaleOrder, self).create(vals)
        return result

    @api.depends('job_number_prefix', 'job_number_sufix', 'job_sequence')
    def _compute_job_number(self):
        for sale_order in self:
            if not sale_order.job_sequence or sale_order.job_sequence == 0:
                sale_order.job_sequence = self.env['ir.sequence'].next_by_code(
                    'sale.order.job.number') or 23500
            sale_order.job_number = str(sale_order.job_number_prefix) + str(
                sale_order.job_sequence) + str(sale_order.job_number_sufix)
