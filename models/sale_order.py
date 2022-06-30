# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _cancel_expired_quotations(self):
        todays_date = fields.Date.today()
        expired_records = self.env['sale.order'].search([('validity_date','!=',False)])
        for record in expired_records:
            if record.validity_date < todays_date or record.is_expired:
                record.action_cancel()
