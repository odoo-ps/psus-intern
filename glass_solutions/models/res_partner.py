# *-* coding: utf-8 *-*

from odoo import models,fields,api


class Partner(models.Model):
    _inherit = "res.partner"
    
    is_sales_person=fields.Boolean(defult=False, compute='_compute_is_readonly')
    
    def _compute_is_sales_person(self):
        for record in self:
            if record.env.user.has_group('sales_team.group_sale_manager'):
                record.is_sales_person = False
            elif (record.env.user.has_group('sales_team.group_sale_salesman_all_leads') or self.env.user.has_group('sales_team.group_sale_salesman')):
                record.is_sales_person = True  
