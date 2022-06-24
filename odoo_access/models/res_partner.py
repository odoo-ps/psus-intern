# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_sales_person = fields.Boolean(
        compute="_compute_is_sales_person", string="Is sales person")

    # function to check if the user is ales_team.group_sale_manager group
    @api.depends()
    def _compute_is_sales_person(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.is_sales_person = False
            return
        if self.env.user.has_group('sales_team.group_sale_salesman') or self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            self.is_sales_person = True
        
