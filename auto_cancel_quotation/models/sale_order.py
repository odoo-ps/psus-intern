# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import date

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _cancel_quotation(self):
        for record in self.env['sale.order'].search(
            [('state', 'in', ['draft', 'sent']), ('validity_date', '<', date.today())]
        ):
            record.update({'state': 'cancel'})