from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'stock.move'
    
    @api.onchange('quantity_done','product_uom_qty')
    def _onchange_quantity_done(self):
        if self.quantity_done >= self.product_uom_qty:
            raise UserError(_("You can't receive more than the ordered quantity. Please, enter another quantity."))
       