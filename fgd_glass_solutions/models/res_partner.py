# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_create_only = fields.Boolean(
        compute='_compute_partner_create_only')

    @api.depends()
    def _compute_partner_create_only(self):
        user = self.env.user
        writable = user.has_group('sales_team.group_sale_manager') or not (
            user.has_group('sales_team.group_sale_salesman') or
            user.has_group('sales_team.group_sale_salesman_all_leads')
        )
        for record in self:
            record.partner_create_only = record.id and not writable
