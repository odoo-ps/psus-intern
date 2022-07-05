# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class StockInventory(models.Model):
    _name = 'stock.inventory'
    _inherit = ['stock.inventory', 'sync.document.status']

    def _import_stock_status(self):
        return self._execute_edi_sync('import_request_inventory')
