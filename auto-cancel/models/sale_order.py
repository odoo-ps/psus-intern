# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Retrieve Sale Order records (self.env['sale.order'])
    # Find Quotations among records (state=draft)
    # Filter expired Quotations (is_expired=True)
    # Cancel Quotations that meet the conditions (action_cancel())
    # Should leave Quotations with no expiration date set alone
    @api.autovacuum
    def _auto_cancel_expired_quotations(self):
        self.env['sale.order'].search(
            ['&', ('state', '=', 'draft'), ('is_expired', '=', True)]
                ).action_cancel()
