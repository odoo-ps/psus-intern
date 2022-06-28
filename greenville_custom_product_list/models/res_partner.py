# -*- coding: utf-8 -*-
from odoo import fields,models,api 


class ResPartner(models.Model):
    _inherit='res.partner'

    product_id = fields.Many2one(
        string='Product List',
        ondelete='set null',
        comodel_name = 'product.list'
    )
    