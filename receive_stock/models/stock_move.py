# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty', 'quantity_done')
    def _onchange_quantity_done(self):
        self.ensure_one()
        if self.quantity_done > self.product_uom_qty:
            raise ValidationError(
                _(f'You can\'t receive more than the ordered quantity. Please, enter another quantity.\nOrdered quantity: {self.product_uom_qty}\nReveived quantity: {self.quantity_done}'))
