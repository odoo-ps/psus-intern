# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(
        string='Pair per case', default=None, required=True)
    price_per_pair = fields.Monetary(
        string='Price per pair', default=None, required=True)
    fields_empty = fields.Boolean(string='Whether one of pair_per_case and price_per_pair is empty', default=False)
    sales_price = fields.Monetary(string='Sales Price', store=True)

    @api.onchange('pair_per_case', 'price_per_pair')
    def _onchange_sales_price(self):
        if self.pair_per_case < 0:
            raise UserError('Pair per case cannot be negative')
        if self.price_per_pair < 0.00:
            raise UserError('Price per pair cannot be negative')
        self.fields_empty = not self.pair_per_case and not self.price_per_pair
        self.sales_price = self.pair_per_case * self.price_per_pair
