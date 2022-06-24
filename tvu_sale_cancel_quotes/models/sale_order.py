# -*- coding: utf-8 -*-

from odoo import models, api
from datetime import date

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def cancel_expired_quotations(self):
        self.search([('state', '=', 'draft'),('validity_date', '!=', False),('validity_date','<',date.today())]).action_cancel()
