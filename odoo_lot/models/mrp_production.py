# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    lot_number = fields.Char(string='Lot Number')

    # when press button mark as done in mrp.production calculate lot number
    def button_mark_done(self):
        # execute super function
        res = super(MRPProduction, self).button_mark_done()
        # check if lot number is empty
        if self.product_id.lot_prefix:
            # get lot number from product
            self.lot_number = self.env['ir.sequence'].next_by_code(
                self.product_id.lot_prefix)
            if not self.lot_number:
                self.lot_number = self.env['ir.sequence'].create({
                    'name': 'Lot Number',
                    'code': self.product_id.lot_prefix,
                    'prefix': self.product_id.lot_prefix,
                    'padding': 5,
                    'number_increment': 1,
                    'company_id': self.company_id.id,
                    'implementation': 'standard',
                }).next_by_code(self.product_id.lot_prefix)
        return res
