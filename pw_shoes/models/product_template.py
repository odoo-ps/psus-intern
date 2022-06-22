# -- coding: utf-8 --

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per case')
    price_per_pair = fields.Float(string='Price per pair')

    list_price = fields.Float(string='Sales price', compute='_compute_list_price', store=True)

    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        for product in self.filtered(lambda x: x.price_per_pair and x.pair_per_case):
            if(product.pair_per_case < 0 or product.price_per_pair < 0):
                raise UserError(_('Pair per case and price per pair must be positive'))
            product.list_price = product.price_per_pair * product.pair_per_case
