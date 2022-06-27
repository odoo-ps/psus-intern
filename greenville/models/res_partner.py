# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_list_ids = fields.Many2one(comodel_name='product.list',
                                        string='Product List')
 