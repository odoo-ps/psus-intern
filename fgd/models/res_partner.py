# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    user_is_sales_administrator = fields.Boolean(
        string = 'User is Administrator',
        compute = '_check_if_user_is_sales_administrator'
    )

    def _check_if_user_is_sales_administrator(self):
        for partner in self:
            user = self.env.user
            partner.user_is_sales_administrator = (user.has_group('limit_sales_access_rights.group_sale_manager'))
