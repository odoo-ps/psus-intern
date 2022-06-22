# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    quantity_per_case = fields.Integer(string='Quantity / Case')
    unit_price = fields.Monetary(string='Unit Price')
    list_price_readonly = fields.Boolean(string="List Price Read-Only")

    @api.onchange('quantity_per_case', 'unit_price')
    def _onchange_list_price(self):
        if self.quantity_per_case or self.unit_price:
            self.list_price_readonly = True
            self.list_price = self.quantity_per_case * self.unit_price
        else:
            self.list_price_readonly = False