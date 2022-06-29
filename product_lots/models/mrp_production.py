# -*- coding: utf-8 -*-
from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    lot_number = fields.Char(string='Lot Number')

  
    def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        if self.product_id.lot_number_prefix:
            if  not self.lot_number:
                self.lot_number = self.env['ir.sequence'].create({
                'name': 'Secuence for Lot Number',
                'code': self.product_id.lot_number_prefix,
                'prefix': self.product_id.lot_number_prefix,
                'padding': 5,
                'implementation': 'standard',
                'number_next': 1,
                "number_increment": 1,
                "active": True,
                }).next_by_code(self.product_id.lot_number_prefix)
            else:
                self.lot_number = self.env['ir.sequence'].next_by_code(self.product_id.lot_number_prefix)
        return res
