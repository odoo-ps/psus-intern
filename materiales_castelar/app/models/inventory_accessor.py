from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class InventoryAccessor(models.Model):
    _inherit = 'stock.move'

    @api.onchange('quantity_done')
    def _check_quantity_done(self):
        _logger.info("Calling _check_quantity_done")
        for picking in self:
            if self.quantity_done > self.product_uom_qty:
                raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity.")
            elif picking.quantity_done < 0:
                raise ValidationError("You can't receive a negative quantity. Please, enter another quantity.")