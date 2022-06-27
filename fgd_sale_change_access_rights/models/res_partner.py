# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    read_only = fields.Boolean(compute='_compute_read_only', string='Read Only')

    @api.depends()
    def _compute_read_only(self):
        
        current_user = self.env.user

        if current_user.has_group('sales_team.group_sale_manager'):
            self.read_only = False
        else:
            self.read_only = True