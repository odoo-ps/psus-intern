# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cancel(models.Model):
    _inherit = 'sale.order'

    @api.model
    def action_cron_auto_cancel(self):
        """ Perform the automatic cancellation of quotations """
        self.env['sale.order'].search([('type_name', '=', 'Quotation')]).action_perform_auto_cancel()


    def action_perform_auto_cancel(self):
        for record in self:
            if record.type == 'Quotation':
                if record.validity_date < fields.Date.today() and record.validity_date:
                    record.state = 'cancel'