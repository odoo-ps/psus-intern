# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _remove_expired_quotations(self):
        for sale_order in self.env['sale.order'].search(
                [
                    ['state', 'in', ('draft', 'sent')],
                    ['validity_date', '!=', False],
                    ['validity_date', '<', fields.Date.today()]
                ]
        ):
            sale_order.action_cancel()
