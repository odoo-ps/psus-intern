# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Number of pairs')
    price_per_pair = fields.Monetary(string='Price per pair')
    list_price_editable = fields.Boolean(string='Whether Sales Price should be editable')
    
    @api.onchange('pair_per_case','price_per_pair')
    def _calculate_sales_price(self):
        if self.pair_per_case or self.price_per_pair:
            self.list_price_editable = False
        else:
            self.list_price_editable = True

        if self.pair_per_case and self.price_per_pair:
            self.list_price = self.pair_per_case * self.price_per_pair