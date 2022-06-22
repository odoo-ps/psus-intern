# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubscriptionAddress(models.Model):
    _inherit = 'sale.subscription'
    
    partner_addr = fields.Many2one(comodel_name='res.partner', string='Partner Address', auto_join=True)
