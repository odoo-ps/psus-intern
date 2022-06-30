# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from traitlets import default

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='pair_per_case')
    price_per_pair = fields.Monetary(string='price_per_pair')

    sales_price = fields.Monetary(string='Sales Price', store = True)

    check_empty = fields.Boolean(string='Check Empty', default=False)


    @api.onchange('pair_per_case','price_per_pair')
    def _onchange_(self):
        self.ensure_one()
        if self.pair_per_case or self.price_per_pair:
            self.check_empty = False
        else:
            self.check_empty = True
        self.sales_price = self.pair_per_case * self.price_per_pair
        