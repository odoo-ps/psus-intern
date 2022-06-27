# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def check_expired(self, quote):
        expire_date = quote.validity_date
        if not expire_date:
            return False
        current_date = fields.Date.today()
        return current_date > expire_date

    def auto_quotation_cancel(self):
        all_quotes = self.search([])
        quotes_to_cancel = all_quotes.filtered(self.check_expired)
        quotes_to_cancel._action_cancel()
