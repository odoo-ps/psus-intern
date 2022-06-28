# -- coding: utf-8 --
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pairs_per_case = fields.Integer(string='Pairs Per Case')

    price_per_pair = fields.Monetary(string='Price Per Pair')

    list_price = fields.Monetary(string='Sales Price',
                            compute='_compute_sales_price',
                            inverse='_inverse_sales_price', 
                            store=True)

    @api.depends('pairs_per_case', 'price_per_pair')
    def _compute_sales_price(self):
        if self.list_price or self.pairs_per_case:
            self.list_price = self.pairs_per_case * self.price_per_pair
        else:
            self.list_price = 0

    def _inverse_sales_price(self):
        if not self.pairs_per_case:
            self.pairs_per_case = 0
        if not self.price_per_pair:
            self.price_per_pair = 0
