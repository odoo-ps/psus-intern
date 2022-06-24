# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def _auto_cancel_quotations(self):
        for sale in self.env['sale.order'].search([('state', '=', 'draft'), ('validity_date', '!=', False), ('is_expired', '!=', False)]).filtered(lambda so: (so.validity_date and so.validity_date < fields.Date.today())):
            sale.action_cancel()
