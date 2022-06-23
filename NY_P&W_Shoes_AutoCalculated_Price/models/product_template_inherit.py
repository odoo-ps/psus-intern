# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_template_inherit(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer('Pair per Case' )

    price_per_pair = fields.Monetary('Price per Pair')

    list_price = fields.Monetary(
        'Sale Price',
        compute ='_compute_list_price'

    )

    @api.depends('pair_per_case', 'price_per_pair')
    def _compute_list_price(self):
        for rec in self:
            rec.list_price = rec.pair_per_case * rec.price_per_pair



