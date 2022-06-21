# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import UserError


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done')
    def _onchange_quantity_demand(self):
        if (self.env.context.get('picking_type_code') == 'incoming' and
            self.product_uom_qty and
                self.quantity_done > self.product_uom_qty):
            raise UserError(
                _("You can't receive more than the ordered quantity. Please, enter another quantity."))
