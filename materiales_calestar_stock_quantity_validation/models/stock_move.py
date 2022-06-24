# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockMove(models.Model):

    _inherit = "stock.move"

    @api.onchange("quantity_done", "product_uom_qty")
    def validate_done_quantity(self):

        if self.quantity_done > self.product_uom_qty:
            raise ValidationError(
                "Value more than Demand. Please ensure that done quantity is lesser than or equal to demand."
            )
