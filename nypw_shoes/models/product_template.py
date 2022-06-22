# -*- utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    currency_id = fields.Many2one('res.currency', string='Currency')
    pair_per_case = fields.Integer(string='Pair Per Case')
    price_per_pair = fields.Monetary(string='Price Per Pair')
    list_price = fields.Monetary(string='Sales Price',
                                 compute='_compute_sales_price')

    @api.depends('pair_per_case', 'price_per_pair')
    def _compute_sales_price(self):
        for record in self:
            if record.pair_per_case > 0 and record.price_per_pair > 0:
                record.list_price = record.pair_per_case * record.price_per_pair
            else:
                record.list_price = 0

    @api.constrains('pair_per_case')
    def _check_pair_per_case(self):
        for record in self:
            if record.pair_per_case < 0:
                raise ValidationError(
                    'Pair Per Case must be larger than or equal to zero.')

    @api.constrains('price_per_pair')
    def _check_price_per_pair(self):
        for record in self:
            if record.price_per_pair < 0.0:
                raise ValidationError(
                    'Price Per Pair must be larger than or equal to zero.')
