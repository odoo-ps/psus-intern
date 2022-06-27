# -*- coding: utf-8 -*-

from odoo import models, api, exceptions


class StockMove(models.Model):
    
    _inherit = 'stock.move'

    @api.onchange('quantity_done')
    def validate_product_qty(self):
        for record in self:
            if record.quantity_done > record.product_uom_qty:
                raise exceptions.ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity")