# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ResPartner(models.Model):
    # _name = "res.part"
    _inherit = "res.partner"
    # _description = "Product List"

    # name = fields.Char(string="Title", required=True)

    product_list_ids = fields.Many2one(
        comodel_name="product.list", string="Customers using list"
    )
