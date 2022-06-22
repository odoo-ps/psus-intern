#-*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    

    
    def confirm_all_RFQs(self):
        rfqs = self.env['purchase.order'].search([('state','=','draft'),('partner_id', '=',1), ('user_id','=',2)])
        for rfq in rfqs:
            rfq.state = 'purchase'
            
