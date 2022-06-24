# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pairs_per_case = fields.Integer(string="Number of pairs of shoes per case")
    price_per_pair = fields.Monetary(string="Price per pair of shoes")
    list_price = fields.Monetary(string='Sales Price')

    @api.onchange('pairs_per_case', 'price_per_pair')
    def _onchange_sales_price(self):
        self.list_price = self.pairs_per_case * self.price_per_pair

    @api.onchange('list_price')
    def _check_sales_price(self):
        if self.pairs_per_case or self.price_per_pair:
            if self.list_price != (self.pairs_per_case * self.price_per_pair):
                self.list_price = self.pairs_per_case * self.price_per_pair
