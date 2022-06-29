# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    final_client = fields.Char('Final Client')
    job_site = fields.Char('Job Site')
    opportunity_id = fields.Many2one('crm.lead', 'Opportunity')
    travel_in = fields.Date('Travel In')
    travel_out = fields.Date('Travel Out')
