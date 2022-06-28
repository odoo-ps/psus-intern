# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def action_generate_serial(self):
        self.ensure_one()
        if self.product_id.lot_prefix:
            last_serial = self.env['stock.production.lot'].search(
                [('company_id', '=', self.company_id.id),
                 ('product_id', '=', self.product_id.id)],
                limit=1, order='id DESC')
            if last_serial:
                self.lot_producing_id = self.env['stock.production.lot'].create({
                    'product_id': self.product_id.id,
                    'company_id': self.company_id.id,
                    'name': int(last_serial.name) + 1
                })
            else:
                self.lot_producing_id = self.env['stock.production.lot'].create({
                    'product_id': self.product_id.id,
                    'company_id': self.company_id.id,
                    'name': int(str(self.product_id.lot_prefix) + '001')
                })
        else:
            self.lot_producing_id = self.env['stock.production.lot'].create({
                'product_id': self.product_id.id,
                'company_id': self.company_id.id
            })
        if self.move_finished_ids.filtered(lambda m: m.product_id == self.product_id).move_line_ids:
            self.move_finished_ids.filtered(
                lambda m: m.product_id == self.product_id).move_line_ids.lot_id = self.lot_producing_id
        if self.product_id.tracking == 'serial':
            self._set_qty_producing()
