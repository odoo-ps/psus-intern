# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    customer_ids = fields.Many2one(comodel_name='res.partner', string='Customers bound to this product')
