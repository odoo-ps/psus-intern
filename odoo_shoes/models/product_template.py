# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per case')
    price_per_pair = fields.Monetary(string='Price per pair')

    state = fields.Selection([('editable', 'Editable'), ('read_only',
                             'Read Only')], 'Status', copy=False, default='editable', readonly=True)

    list_price = fields.Float(compute='_compute_list_price',
                              store=True,
                              states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]})

    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        self.ensure_one()
        if self.pair_per_case == 0 or self.price_per_pair == 0:
            self.state = 'editable'
        # check that price_per_pair is not negative
        if self.price_per_pair < 0:
            raise ValidationError(_('Price per pair must be positive'))
        # check that pair_per_case is not negative
        if self.pair_per_case < 0:
            raise ValidationError(_('Pairs per case must be positive'))
        self.list_price = self.price_per_pair * self.pair_per_case
        if self.pair_per_case != 0 and self.price_per_pair != 0:
            self.state = 'read_only'
