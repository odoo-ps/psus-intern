# -*- coding: utf-8 -*-

from odoo import models, fields, api

class propertycopier(models.Model):
    _inherit = 'sale.subscription'

    partner_record = fields.Many2one(
        'res.partner',
        string = "Customer Record"
    )

    def _prepare_invoice_data(self):
        result = super(propertycopier, self)._prepare_invoice_data()
        result['partner_id'] = self.partner_record.id
        return result
