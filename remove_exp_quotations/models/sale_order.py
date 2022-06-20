# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.autovacuum
    def _cancel_exp_quotations(self):
        quotations = self.env['sale.order'].search(
            [('validity_date', '!=', None), ('validity_date', '<', date.today()), ('is_expired', '=', True)])
        for quotation in quotations:
            quotation.write(
                {'state': 'cancel'}
            )
