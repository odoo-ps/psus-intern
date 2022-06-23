# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ppc = fields.Integer(string="Pair per Case")
    ppp = fields.Monetary(string="Price per Pair")
    list_price = fields.Float(
        'Sales Price', default=0,
        digits='Product Price',
        help="Price at which the product is sold to customers.",
        compute="_compute_sales_price",
        inverse="_make_editable",
        store=True,
    )

    @api.depends('ppc', 'ppp')
    def _compute_sales_price(self):
        for rec in self:
            rec.list_price = rec.ppc * rec.ppp

    def _make_editable(self):
        return
