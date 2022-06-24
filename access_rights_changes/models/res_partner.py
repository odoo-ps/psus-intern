# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_partner_id_readonly = fields.Boolean(compute='_compute_is_partner_id_readonly',
                                            inverse='_inverse_is_partner_id_readonly',
                                            readonly=True)

    @api.depends()
    def _compute_is_partner_id_readonly(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.is_partner_id_readonly = False
            return
        elif (self.env.user.has_group('sales_team.group_sale_salesman_all_leads') or self.env.user.has_group('sales_team.group_sale_salesman')):
            self.is_partner_id_readonly = True

    def _inverse_is_partner_id_readonly(self):
        pass
