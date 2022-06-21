# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMove(models.Model):
    _inherit = 'stock.move'

    validate_qty_lt_demand = fields.Boolean('Validate Quantity less than Demand',
                                            required=True, default=True)

    @api.onchange('quantity_done')
    def _onchange_quantity_demand(self):
        if self.validate_qty_lt_demand and self.quantity_done > self.product_uom_qty:
            raise UserError(
                _("You can't receive more than the ordered quantity. Plesae, enter another quantity."))
