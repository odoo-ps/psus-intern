# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_list_id = fields.Many2one(comodel_name='product.list',
                                      string='Product List')
