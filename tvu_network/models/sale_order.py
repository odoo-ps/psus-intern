# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # cancelled the quotations that are expired every day
    @api.autovacuum
    def _remove_quotation_if_expired_autovacuum(self):
        # use the action_cancel() function
        self.env['sale.order'].search(
            [('state', '=', 'draft'), ('validity_date', '<', fields.Date.today())]).action_cancel()
