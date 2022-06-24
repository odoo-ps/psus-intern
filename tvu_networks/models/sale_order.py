# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _remove_expired_quotations(self):
        self.search([
            ('state', 'in', ['draft', 'sent']),
            ('validity_date', '!=', False),
            ('validity_date', '<', fields.Date.today()),
        ]).action_cancel()
