# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    #TODO check why it's making me create res_partner from scratch
    product_list_id = fields.Many2one(comodel_name='product.list', string='Product List')
