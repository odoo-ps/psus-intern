# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def set_state(self, state):
        self.state = state

    def cancel_old_quotations(self):
        today = fields.Date.today()
        records = self.env["sale.order"].search([])
        old_quotations = records.filtered(lambda r: r.validity_date).filtered(lambda r: r.validity_date < today) #
        for record in old_quotations:
            record.set_state("cancel")
