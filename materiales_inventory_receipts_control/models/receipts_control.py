# -*- coding utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ReceiptsControl(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done')
    def _onchange_quantity_done(self):
        if self.quantity_done > self.product_uom_qty:
            raise ValidationError(_('You can\'t receive more than the ordered quantity. Please, enter another quantity.'))
