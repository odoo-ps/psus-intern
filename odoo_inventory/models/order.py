# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Order(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty','quantity_done')
    def _onchange_quantity_done(self):
        if self.quantity_done > self.product_uom_qty:
            raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity.")
