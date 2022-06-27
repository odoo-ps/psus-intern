# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_create_only = fields.Boolean(
        compute='_compute_partner_create_only')

    def _compute_partner_create_only(self):
        for record in self:
            record.partner_create_only = (
                not record.has_group('sales_team.group_sale_manager') and
                (record.has_group('sales_team.group_sale_salesman') or
                 record.has_group('sales_team.group_sale_salesman_all_leads'))
            )
