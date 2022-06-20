#-*- coding: utf-8 -*-
from attr import field
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
class AutoCancel(models.Model):
    _inherit = "sale.order"
    test = fields.Char(string="test");
    @api.autovacuum
    def _remove_quotations(self):
        print("here!!!!!!!!!!!!!!!!!!", type(self))
        
        print(self.validity_date)
            
        self.env['sale.order'].search([('state', '=', 'draft'),('validity_date', '<', fields.Date.today())
         ]).write({'state': 'cancel'})