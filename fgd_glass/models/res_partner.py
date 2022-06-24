# -*- coding: utf-8 -*-
from odoo import models, fields

#class that inherits from the res_partner model
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_read_only = fields.Boolean(string="Is read only", compute='_compute_is_read_only', store=False)


    def _compute_is_read_only(self):
        for partner in self:
            partner.is_read_only = True
            if partner.env.user.has_group ('sales_team.group_sale_salesman_all_leads') or partner.env.user.has_group ('sales_team.group_sale_salesman'):
                partner.is_read_only = True 
            if partner.env.user.has_group ('sales_team.group_sale_manager'):
                partner.is_read_only = False
