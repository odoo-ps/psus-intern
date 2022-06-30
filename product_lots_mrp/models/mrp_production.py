from odoo import models, fields
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    lot_number = fields.Char(string='Lot Number', readonly=True)
    
    def button_mark_done(self):
        action = super(MrpProduction, self).button_mark_done()

        if self.product_id.lot_prefix and not self.lot_number:
            self.lot_number = self.env['ir.sequence'].next_by_code(self.product_id.lot_prefix)
            if not self.lot_number:
                self.lot_number = self.env['ir.sequence'].create({
                    'name': f'lot.{self.product_id.lot_prefix}',
                    'code': self.product_id.lot_prefix,
                    'prefix': self.product_id.lot_prefix,
                    'padding': 2,
                }).next_by_code(self.product_id.lot_prefix)

        return action

    def action_generate_lot(self):
        if self.product_id.lot_prefix:
            self.lot_number = self.env['ir.sequence'].next_by_code(self.product_id.lot_prefix)
            if not self.lot_number:
                self.lot_number = self.env['ir.sequence'].create({
                    'name': f'lot.{self.product_id.lot_prefix}',
                    'code': self.product_id.lot_prefix,
                    'prefix': self.product_id.lot_prefix,
                    'padding': 2,
                }).next_by_code(self.product_id.lot_prefix)
        else:
            raise UserError("Product must have a lot number prefix to be assigned a lot number")
