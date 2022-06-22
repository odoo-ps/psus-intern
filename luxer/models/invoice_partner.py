# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubscriptionAddress(models.Model):
    _inherit = 'account.move'

    new_partner = fields.Many2one('res.partner', compute='add_new_partner_address', string='Partner Address', store=True)

    @api.depends('partner_id')
    def add_new_partner_address(self):
        for rec in self:
            res = self.env['sale.subscription'].search([('code', '=', rec.invoice_origin)])
            rec.new_partner = res.partner_addr