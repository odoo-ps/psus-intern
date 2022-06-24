# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    price_per_pair = fields.Float(string='Price Per Pair', default=0.00)
    pair_per_case = fields.Integer(string='Pair Per Case', default=0)

    list_price = fields.Float(string='Sales Price', default=1.0, digits='Product Price', help="Price at which the product is sold to customers.", compute='_compute_list_price', store=True)
    
    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        self.list_price = self.price_per_pair * self.pair_per_case

    