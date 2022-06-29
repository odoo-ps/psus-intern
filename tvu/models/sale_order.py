# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class tvu(models.Model):
    _inherit = "sale.order"

    def AutoCancelExpiredQuotations(self):
        today = date.today()
        ids = self.env['sale.order'].search(["&",['validity_date','<=',today],['state','=','draft']])
        for id in ids:
            id.write({'state':'cancel'})
