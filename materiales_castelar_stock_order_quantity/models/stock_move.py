# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done','product_uom_qty')
    def _check_received_quantity(self):
        if (self.picking_type_id.code == 'incoming'):
            if self.quantity_done > self.product_uom_qty:
                raise UserError("You can't receive more than the ordered quantity. Please, enter another quantity")