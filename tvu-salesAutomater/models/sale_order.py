# -*- coding:utf-8 -*-


from datetime import date
from odoo import models, fields, api
import logging 

class SalesOrder(models.Model):
    _inherit = 'sale.order'


    def delete_invoice_after_exp_date(self):
        self.env['sale.order'].search([('state', '=', 'draft'),('validity_date', '<', fields.Date.today())]).write({'state': 'cancel'})


