#-*- coding:utf-8  -*-
from odoo import fields, models,api
from odoo.exceptions import UserError


class StockReceipt(models.Model):
    #inherited from object stock.move
    _inherit='stock.move'
    
    #onchange if quantity_done field has been modified
    @api.onchange('quantity_done')
    def _onchange_validate_quantity_done(self): 
        if self.quantity_done>self.product_uom_qty:
            raise UserError("You can't receive more than the ordered quantity. Please, enter another quantity")
                