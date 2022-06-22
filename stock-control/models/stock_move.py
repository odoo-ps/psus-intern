# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.depends('quantity_done', 'product_uom_qty')
    def _compute_product_demand(self):
        self.ensure_one()
        if self.picking_code == 'incoming' and \
                self.quantity_done > self.product_uom_qty:
            raise ValidationError("""
                You can't receive more than the ordered quantity.\
                Please, enter another quantity.
            """)
