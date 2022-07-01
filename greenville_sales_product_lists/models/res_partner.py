# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    product_list_ids = fields.Many2one(
        comodel_name="product.list", string="Customers using list"
    )
