# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done', 'product_uom_qty')
    def _check_recieved_less_than_demand(self):
        for record in self:
            if record.quantity_done > record.product_uom_qty:
                raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity")