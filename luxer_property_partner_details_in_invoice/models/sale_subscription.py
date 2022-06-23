# -*- coding: utf-8 -*-
from odoo import models,fields,api


class SaleSubscription(models.Model):
    _inherit= "sale.subscription"
    property_partner_id = fields.Many2one('res.partner', string='Property Partner', required=False, auto_join=True)

    def _prepare_invoice_data(self):
        """
        replacing the partner id with the property partner while preparing invoice
        """
        self.ensure_one()
        res = super(SaleSubscription,self)._prepare_invoice_data()
        res['partner_id'] = self.property_partner_id.id or res.get(
            'partner_id')
        return res