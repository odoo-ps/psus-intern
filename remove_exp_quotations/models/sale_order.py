# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_cron_auto_cancel(self):
        for sale_order in self:
            if sale_order.state == 'Quotation' and sale_order.validity_date:
                if sale_order.validity_date < date.today() or sale_order.is_expired:
                    sale_order.action_cancel()
                    sale_order.state = 'Cancelled'
                    sale_order.is_expired = True
