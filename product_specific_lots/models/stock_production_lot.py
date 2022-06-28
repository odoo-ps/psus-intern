# -*- coding: utf-8 -*-

from odoo import models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    def _get_next_serial(self, company, product):
        if product.tracking == "serial" or product.tracking == "lot":
            last_serial = self.env['stock.production.lot'].search(
                [('company_id', '=', company.id), ('product_id', '=', product.id)],
                limit=1, order='id DESC')
            if product.lot_prefix and not (last_serial and last_serial.name.startswith(product.lot_prefix)):
                return self.env['stock.production.lot'].generate_lot_names(product.lot_prefix + '0', 2)[1]
            if last_serial:
                return self.env['stock.production.lot'].generate_lot_names(last_serial.name, 2)[1]       
        return False
