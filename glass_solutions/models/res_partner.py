# *-* coding: utf-8 *-*

from multiprocessing.dummy import current_process
from odoo import models,fields,api


class Partner(models.Model):
    _inherit = "res.partner"
    
    is_sales_person=fields.Boolean(defult=False, compute='_compute_is_readonly',store=False)
    
    
    def _compute_is_readonly(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.is_sales_person = False
            return
        elif (self.env.user.has_group('sales_team.group_sale_salesman_all_leads') or self.env.user.has_group('sales_team.group_sale_salesman')):
            self.is_sales_person = True

            
         
        
