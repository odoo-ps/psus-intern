# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Quote(models.Model):

    _inherit = 'sale.order'

    @api.model
    def _check_quote(self):
        for sale in self.env['sale.order'].search([('state', '=', 'draft')]):
            if sale.validity_date and sale.validity_date < fields.Date.today():
                sale.action_cancel()
