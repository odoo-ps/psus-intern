from odoo import models, api, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Demo purposes only
    product_gender = fields.Selection([
        ('svelte', 'Svelte'),
        ('creative', 'Creative'),
        ('power', 'Power'),
        ('relaxed', 'Relaxed'),
        ('eccentric', 'Eccentric')
    ], required=True, default='svelte')
    upc_seq = fields.Many2one('ir.sequence', compute='_compute_upc_seq')
    barcode = fields.Char(compute='_compute_barcode', store=True)

    @api.model
    def create(self, values):
        if isinstance(values, list):
            for value in values:
                self._assign_name(value)
        else:
            self._assign_name(values)
        return super().create(values)

    @api.model
    def _assign_name(self, value: dict):
        """Assigns a name to the product based on the category sequence."""
        if not value.get('name') and value.get('categ_id'):
            value['name'] = self.env['ir.sequence'].browse(
                value['categ_id']).next_by_id()

    @api.onchange('categ_id')
    def _onchange_categ(self):
        if self.id and self.categ_id:
            self.name = self.categ_id.next_name()

    @api.depends('product_gender')
    def _compute_upc_seq(self):
        for record in self:
            prefix = record.product_gender[:3].upper()
            seq = self.env['ir.sequence'].search(
                [('code', '=', prefix)])
            if not seq:
                seq = self.env['ir.sequence'].create({
                    'code': prefix,
                    'name': record.product_gender,
                    'prefix': prefix,
                    'padding': 5
                })
            record.upc_seq = seq

    @api.depends('upc_seq')
    def _compute_barcode(self):
        for record in self:
            if record.upc_seq:
                record.barcode = record.upc_seq.next_by_id()
