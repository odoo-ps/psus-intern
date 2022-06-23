# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done')
    def _onchange_quantity_check(self):
        if self.quantity_done > self.product_uom_qty:
            raise UserError("Entered quantity must be equal to or smaller than the demand")
            