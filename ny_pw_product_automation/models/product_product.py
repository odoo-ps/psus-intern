# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_gender = fields.Many2one(string='Product Gender', comodel_name='nypw.product.gender')

    @api.onchange('product_gender')
    def _onchange_product_gender(self):
        if self.product_gender and self.product_gender.upc_sequence:
            self.default_code = self.product_gender.upc_sequence.next_by_id()


    @api.onchange('categ_id')
    def _onchange_category(self):
        if self.categ_id.sequence:
            self.name = self.categ_id.sequence.next_by_id()