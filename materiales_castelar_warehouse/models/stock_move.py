# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import ValidationError

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty', 'quantity_done')
    def _compare_receipt_with_order(self):
        if self.quantity_done > self.product_uom_qty:
            print(type(self.quantity_done))
            err_str = ('You can\'t receive more than the ordered quantity. Please, enter another quantity.\n\t {} > {}'.format(self.quantity_done, self.product_uom_qty))
            raise ValidationError(err_str)
