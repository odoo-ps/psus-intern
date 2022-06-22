# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(
        string='Pair per case', default=None, required=True)
    price_per_pair = fields.Monetary(
        string='Price per pair', default=None, required=True)
    sales_price = fields.Monetary(
        compute='_compute_sales_price', string='Sales Price', store=True)

    @api.constrains('pair_per_case', 'price_per_pair')
    def _check_pair_and_price(self):
        if self.pair_per_case < 0:
            raise ValidationError('Pair per case cannot be negative')
        if self.price_per_pair < 0.00:
            raise ValidationError('Price per pair cannot be negative')

    @api.depends('pair_per_case', 'price_per_pair')
    def _compute_sales_price(self):
        self.sales_price = self.pair_per_case * self.price_per_pair
