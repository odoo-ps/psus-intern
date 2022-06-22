# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    contact_id = fields.Many2one('res.partner', 'Contact')

    def _prepare_invoice_data(self):
        data = super(SaleSubscription, self)._prepare_invoice_data()
        if self.contact_id:
            data['partner_shipping_id'] = self.contact_id.id
        raise Exception(data)
