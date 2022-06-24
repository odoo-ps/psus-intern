# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

#class that inherits from the res_partner model
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_read_only = fields.Boolean(string="Is read only", compute='_is_read_only', store=False)


    def _is_read_only(self):
        for user in self:
            if user.env.user.has_group ('sales_team.group_sale_salesman_all_leads') or user.env.user.has_group ('sales_team.group_sale_salesman'):
                user.is_read_only = True 
            if user.env.user.has_group ('sales_team.group_sale_manager'):
                user.is_read_only = False
