# *-* coding: utf-8 *-*

from odoo import models,fields,api


class Partner(models.Model):
    _inherit = "res.partner"
    
    is_sales_admin=fields.Boolean(default=False, compute='_set_readonly',store=False)
    
    @api.depends()
    def _set_readonly(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.is_sales_admin = True
            return
        elif (self.env.user.has_group('sales_team.group_sale_salesman_all_leads') or self.env.user.has_group('sales_team.group_sale_salesman')):
            self.is_sales_admin = False
