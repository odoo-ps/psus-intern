# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubscriptionAddress(models.Model):
    _inherit = 'sale.subscription'

    partner_addr = fields.Many2one(comodel_name='res.partner', string='Partner Address', auto_join=True)


    def _prepare_invoice_data(self):
        res = super(SubscriptionAddress, self)._prepare_invoice_data()
        res['partner_id'] = self.partner_addr if self.partner_addr else res.get('partner_id')
        return res