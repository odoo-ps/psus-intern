#-*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    

    
    def confirm_all_RFQs(self):
        
        odoobot = self.env.ref('base.partner_root')
        mindesa = self.env.ref('base.main_partner')
        rfqs = self.env['purchase.order'].search([('state','=','draft'),('partner_id', '=',mindesa.id), ('user_id','=',odoobot.id)])
        for rfq in rfqs:
            rfq.button_confirm()
            
