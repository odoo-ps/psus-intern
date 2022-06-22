# -*- coding: utf-8 -*-
from odoo import models,fields,api

class CopyPropertyPartnerDetailsToInvoice(models.Model):
    _inherit= "sale.subscription"
    property_partner = fields.Many2one('res.partner', string='Property Partner', required=False, auto_join=True)

