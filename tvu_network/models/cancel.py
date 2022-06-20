# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cancel(models.Model):
    _inherit = 'sale.order'

    #check if the quotation is expired
    @api.autovacuum
    def _check_expired(self):
        self.env['sale.order'].search([('state', '=', 'draft')]).filtered(lambda r: r.validity_date and r.validity_date < fields.Date.today()).action_cancel()
