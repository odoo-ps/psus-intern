# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import exceptions, api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.depends('quantity_done', 'product_uom_qty')
    def compute_product_demand(self):
        self.env['stock.move'].search([('state', '=', 'draft')])
