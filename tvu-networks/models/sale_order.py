# -*- coding: utf-8 -*-
from odoo import models,fields,api
# from datetime import datetime
# from logger import logging 
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    def _auto_cancel_expired_record(self):
        self.env['sale.order'].search([('state', '=', 'draft'),('validity_date', '<', fields.Date.today())]).write({'state': 'cancel'})