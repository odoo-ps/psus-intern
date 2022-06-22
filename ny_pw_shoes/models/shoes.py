# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Shoes(models.Model):
    _inherit = 'product.template'


    pair_per_case = fields.Integer(string="Pair per case", default=None)

    price_per_pair = fields.Float(string="Price per pair", default=None)

    sales_price = fields.Float(string="Sale Price", store=True)

    fields_empty = fields.Boolean(string="Check pair_per_case or price_per_pair is empty", default=False)

    @api.onchange('pair_per_case', 'price_per_pair')
    def _onchange_sales_price(self):
        if not self.price_per_pair and not self.pair_per_case:
            self.fields_empty = True
        else:
            self.fields_empty = False
        self.sales_price = self.pair_per_case * self.price_per_pair
    

