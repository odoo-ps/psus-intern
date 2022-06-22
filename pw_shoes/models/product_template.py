# -- coding: utf-8 --
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per case')
    price_per_pair = fields.Float(string='Price per pair')

    list_price = fields.Float(string='Sales price', compute='_compute_list_price',
                              store=True,
                              states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]})
    state = fields.Selection([('editable', 'Editable'), ('read_only',
                                                         'Read Only')], 'Status', copy=False, default='editable')

    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        if(self.price_per_pair < 0 or self.pair_per_case < 0):
            raise ValidationError(
                ('Price per pair and pair per case must be positive'))
        else:
            self.state = 'read_only'
        for record in self.filtered(lambda r: r.price_per_pair and r.pair_per_case):
            record.list_price = record.price_per_pair * record.pair_per_case
