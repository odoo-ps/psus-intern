# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pair_per_case = fields.Integer(
        string='Number of pair in the case'
    )

    price_per_pair = fields.Monetary(
        string='Price Per Pair'
    )

    sale_price = fields.Float(
        string="Sale Price",
        compute="_compute_sale_price",
    )

    @api.onchange('pair_per_case', 'price_per_pair')
    def _compute_sale_price(self):
        print(self.pair_per_case == 0)
        print(self.price_per_pair == 0)
        self.sale_price = self.pair_per_case * self.price_per_pair
