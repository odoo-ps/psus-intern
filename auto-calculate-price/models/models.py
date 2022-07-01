# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):

    _inherit = 'product.template'
    
    pair_per_case = fields.Integer(string="Pairs of shoes in a case")
    price_per_pair = fields.Float(string="Price of a pair of shoes")

    list_price = fields.Float(
            'Sales Price', default=1.0,
            digits='Product Price',
            help="Price at which the product is sold to customers.",
            compute="_compute_sales_price"
        )

    @api.depends('pair_per_case', 'price_per_pair')
    def _compute_sales_price(self):
        self.list_price = self.pair_per_case * self.price_per_pair
