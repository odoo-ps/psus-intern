# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.autovacuum
    def _cancel_quotations(self):
        for sale in self.env['sale.order'].search(['state', '=', 'draft'], ['validity_date', '!=', False]).filtered(lambda s: ((s.validity_date and s.validity_date < fields.Date.today()))):
            sale.action_cancel()
