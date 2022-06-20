# *-* coding: utf-8 *-*

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    
    @api.onchange('quantity_done')
    def check_quantity_done(self):
        if (self.quantity_done > self.product_uom_qty) and self.picking_code == 'incoming':
            raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity")   