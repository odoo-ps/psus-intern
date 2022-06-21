# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.autovacuum
    def _cancel_exp_quotations(self):
        self.ensure_one()
        quotations = self.env['sale.order'].search(
            [('is_expired', '=', True)])
        quotations.auto_cancel()
