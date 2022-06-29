# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    product_list_id = fields.Many2one(string='Product List', comodel_name='product.list')
    