# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string="Pair_Per_Case", default=0)
    price_per_pair = fields.Monetary(string="Price_Per_Pair", default=0)
    list_price = fields.Float(
        string='Sales Price',
        digits='Product Price',
        help="Price at which the product is sold to customers.",
        compute='_compute_final_price',
        store=True
    )

    @api.onchange('pair_per_case', 'price_per_pair')
    def _compute_final_price(self):
        self.list_price = self.pair_per_case*self.price_per_pair