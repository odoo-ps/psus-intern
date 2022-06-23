# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StockAssignSerialNumbers(models.Model):
    _inherit = 'stock.move'

    @api.constrains('quantity_done')
    def _onchange_qty(self):
        for ml in self:
            if ml.quantity_done > ml.product_uom_qty:
                raise ValidationError(_("You can't receive more than the ordered quantity. Please, enter another quantity"))
