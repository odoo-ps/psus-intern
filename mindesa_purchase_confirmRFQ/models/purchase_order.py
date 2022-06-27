# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date

class Cancellation(models.Model):
    _inherit = "purchase.order"

    def _rfq_to_po(self):
        client_set = self.env['res.partner'].search([('name','=','Mindesa SAPI de CV')])
        
        filtered_set = client_set.search([('user_id','=',self.env.ref('base.user_root').id)])
        filtered_set.button_confirm()


