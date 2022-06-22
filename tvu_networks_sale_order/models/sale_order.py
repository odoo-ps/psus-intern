# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _cancel_expired_quotations(self):
        self.search([('state', 'in', ['draft', 'sent']),
                     ('validity_date', '<', fields.Date.today())]).action_cancel()
