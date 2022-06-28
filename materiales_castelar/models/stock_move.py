# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.constrains('quantity_done')
    def _check_quantity_done(self):
        """check whether `quantity_done` is less than or equal to `product_uom_qty`"""
        for record in self:
            if record.quantity_done > record.product_uom_qty:
                raise ValidationError(
                    f'"Done" must be smaller than or equal to "Demand" ({record.product_uom_qty}). \n Please enter the correct quantity.)')
            # the constraint that record.quantity_done must not be negative
            # is already set in original stock.move model
