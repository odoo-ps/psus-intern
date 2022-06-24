# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_readonly = fields.Boolean(compute='_change_readonly_fields')

    @api.depends()
    def _change_readonly_fields(self):
        current_user = self.env.user

        if current_user.has_group('sales_team.group_sale_manager') or current_user.has_group('user_admin'):
            self.is_readonly = False
        elif current_user.has_group('sales_team.group_sale_salesman') or current_user.has_group(' 	sales_team.group_sale_salesman_all_leads'):
            self.is_readonly = True
        else:
            self.is_readonly = True
