from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Order(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty','quantity_done')
    def _onchange_quantity_done(self):
        self.ensure_one()
        if self.picking_code == 'incoming':
            if self.quantity_done > self.product_uom_qty:
                raise ValidationError(_("Error you cant output more than the order quantity"))
