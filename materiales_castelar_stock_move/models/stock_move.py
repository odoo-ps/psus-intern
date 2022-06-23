# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.constrains('quantity_done')
    def _check_qty_demand(self):
        if self.search([
            ('picking_id.picking_type_code', '=', 'incoming'),
            ('product_uom_qty', '!=', None),
            ('quantity_done', '>', 'product_uom_qty')
        ]):
            raise ValidationError(_(
                "You can't receive more than the ordered quantity. Please, enter another quantity."))
