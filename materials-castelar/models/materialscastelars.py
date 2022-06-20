from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Order(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty','quantity_done')
    def _onchange_quantity_done(self):
        if self.picking_code == 'incoming':
            if self.quantity_done > self.product_uom_qty:
                raise ValidationError("Error you cant output more than the order quantity")