# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    products_list_id = fields.Many2one(
        comodel_name='greenville.products_list', string='Product List')
