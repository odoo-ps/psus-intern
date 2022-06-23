# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _auto_cancel_expired_record(self):
        self.search([('state', 'in', ['draft','sent']),('validity_date', '<', fields.Date.today())]).action_cancel()