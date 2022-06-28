# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_sales_person = fields.Boolean(compute='_compute_is_sales_person',
                                     readonly=True)

    def _compute_is_sales_person(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.is_sales_person = False
        elif (self.env.user.has_group('sales_team.group_sale_salesman_all_leads') or self.env.user.has_group('sales_team.group_sale_salesman')):
            self.is_sales_person = True
