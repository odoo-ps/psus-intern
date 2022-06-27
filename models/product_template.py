# -*- coding: utf-8 -*-

from odoo import fields,api,models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per Case')
    price_per_pair = fields.Monetary(string="Price per Pair")
    list_price = fields.Float(compute='_compute_sale_price', inverse='_set_list_price', store=True)

    @api.depends('pair_per_case','price_per_pair')
    def _compute_sale_price(self):
        self.list_price = self.pair_per_case * self.price_per_pair
    
    def _set_list_price(self):
        pass