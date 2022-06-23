# -*- encoding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import ValidationError

class shoeCase(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Shoes per case')
    price_per_pair = fields.Monetary(string='Price per shoe')
    sales_price = fields.Monetary(string='Total sales price',compute='_compute_case_price',store=True)
    fields_empty = fields.Boolean(default=True,compute='_check_fields_empty')

    @api.depends('pair_per_case','price_per_pair')
    def _compute_case_price(self):
        for record in self:
            if record.pair_per_case or record.price_per_pair:
                record.sales_price = record.pair_per_case * record.price_per_pair

    @api.depends('pair_per_case','price_per_pair')
    def _check_fields_empty(self):
        for record in self:
            if record.pair_per_case or record.price_per_pair:
                record.fields_empty = False
            else:
                record.fields_empty = True