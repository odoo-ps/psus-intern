# -*- coding: utf-8 -*-
from odoo import models,fields,api
<<<<<<< HEAD

=======
# from datetime import datetime
# from logger import logging 
>>>>>>> parent of cf12d15 (Auto Cancel The Expired Quotations)
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _auto_cancel_expired_record(self):
        self.search([('state', 'in', ['draft','sent']),('validity_date', '<', fields.Date.today())]).action_cancel()