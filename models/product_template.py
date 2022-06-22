# -*- coding: utf-8 -*-

from unittest import skip
from odoo import models,fields,api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    pair_per_case = fields.Integer(string="Pair per case", inverse = '_inverse_sales_price1')

    price_per_pair = fields.Monetary(string="Price per pair", inverse = '_inverse_sales_price2')
    sales_price = fields.Integer(string="Sales price calculated", default="0")

    def _inverse_sales_price1(self):
        for record in self:
            if record.pair_per_case and record.price_per_pair:
                record.sales_price = record.pair_per_case * record.price_per_pair
            else:
                continue
    def _inverse_sales_price2(self):
        for record in self:
            if record.pair_per_case and record.price_per_pair:
                record.sales_price = record.pair_per_case * record.price_per_pair
            else:
                continue
            