# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    user_is_sales_administrator = fields.Boolean(
        string = 'User is Administrator',
        compute = '_check_if_user_is_sales_administrator'
    )

    def _check_if_user_is_sales_administrator(self):
        for record in self:
            user = self.env['res.users'].browse(record._uid)
            record.user_is_sales_administrator = (user.has_group('limit_sales_access_rights.group_sales_administrator') 
                or user.has_group('limit_sales_access_rights.group_sales_administrator_commission'))
