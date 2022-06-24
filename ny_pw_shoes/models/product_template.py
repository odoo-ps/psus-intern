# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string="Pair per case", default=None)

    price_per_pair = fields.Monetary(string="Price per pair", default=None)

    sales_price = fields.Monetary(string="Sale Price", compute='_calc_sales_price', store=True)

    @api.depends('pair_per_case', 'price_per_pair')
    def _onchange_sales_price(self):
        if self.pair_per_case < 0:
            raise ValidationError('Pair per case cannot be negative')
        if self.price_per_pair < 0.00:
            raise ValidationError('Price per pair cannot be negative')
 
    @api.depends('pair_per_case', 'price_per_pair')
    def _calc_sales_price(self):
        for sale in self:
            sale.sales_price = sale.pair_per_case * sale.price_per_pair
    

