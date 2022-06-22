# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.autovacuum
    def _auto_cancel_expired_quotations(self):
        self.env['sale.order'].search(
            [('state', '=', 'draft')]).filtered(
                lambda order: order.is_expired).action_cancel()
