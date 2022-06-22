# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    pair_per_case = fields.Integer(string='Pair per Case')
    price_per_pair = fields.Monetary(string='Price per Pair')

    list_price = fields.Float(compute='_compute_list_price',
                              inverse='_inverse_list_price',
                              store=True,
                              states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]})

    state = fields.Selection([('editable', 'Editable'), ('read_only',
                             'Read Only')], 'Status', copy=True, default='editable', readonly=True)

    @api.depends('pair_per_case', 'price_per_pair')
    def _compute_list_price(self):
        for product in self:
            if product.pair_per_case or product.price_per_pair:
                product.list_price = product.pair_per_case * product.price_per_pair
                product.state = 'read_only'
            else:
                product.state = 'editable'

    def _inverse_list_price(self):
        for product in self:
            if not product.pair_per_case:
                product.pair_per_case = 0
            if not product.price_per_pair:
                product.price_per_pair = 0
