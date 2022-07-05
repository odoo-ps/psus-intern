# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'
    @api.onchange('quantity_done')
    def _doing_something(self):
        if (self.picking_type_id.code == "incoming"):
            if self.quantity_done > self.product_uom_qty:
                raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity.")   
        
