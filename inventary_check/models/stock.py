# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Strock(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty', 'quantity_done')
    def _onchange_qty(self):
        if self.quantity_done > self.product_uom_qty:
            raise ValidationError(_("You can't receive more than the ordered quantity. Please, enter another quantity"))