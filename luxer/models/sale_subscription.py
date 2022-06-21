# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleSubscription(models.Model):
  _inherit = 'sale.subscription'

  partners = fields.Many2many(comodel_name='res.partner', string='Partners')
