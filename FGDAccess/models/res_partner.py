# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):

    is_readonly = fields.Boolean(compute='_change_readonly_fields')

    def _change_readonly_fields(self):
        current_user = self.env.user

        if current_user.has_group('salesperson'):
            self.is_readonly = True
        else:
            self.is_readonly = False

