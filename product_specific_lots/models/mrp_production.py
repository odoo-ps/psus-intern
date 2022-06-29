# *-* coding: utf-8 *-*
from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    lot_number = fields.Char(string='Lot number')

    def button_mark_done(self):
        if self.product_id.lot_number_prefix:
            sequence = self.env['ir.sequence'].search([('code', '=', self.product_id.code)])
            if not sequence:
                sequence = self.env['ir.sequence'].create({
                    'name': 'Lot Number Sequence for ' + self.product_id.code,
                    'implementation': 'standard',
                    'code': self.product_id.code,
                    'prefix': self.product_id.lot_number_prefix,
                    'padding': 5,
                    'number_next': 1,
                    'number_increment': 1,
                })
            self.lot_number = sequence.next_by_code(self.product_id.code)
        return super().button_mark_done()
