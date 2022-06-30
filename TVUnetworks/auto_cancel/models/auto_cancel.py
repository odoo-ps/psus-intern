# -*- coding: utf-8 -*-
from odoo import models
from odoo.fields import Date


class Cancellation(models.Model):
    _inherit = "sale.order"

    def _cancel_expired_record(self):
        
        for record in self.search([('state','=','draft')]):
            if record.validity_date and record.validity_date < Date.today():
                    record.action_cancel()

