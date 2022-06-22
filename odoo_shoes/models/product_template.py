# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per case')
    price_per_pair = fields.Monetary(string='Price per pair')

    list_price = fields.Float(string='Sales price', compute='_compute_list_price',
     store=True,)

    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        #check that price_per_pair is not negative
        if self.price_per_pair < 0:
            raise ValidationError(_('Price per pair must be positive'))
        #check that pair_per_case is not negative
        if self.pair_per_case < 0:
            raise ValidationError(_('Pairs per case must be positive'))
        for record in self.filtered(lambda r: r.price_per_pair and r.pair_per_case):
            record.list_price = record.price_per_pair * record.pair_per_case
