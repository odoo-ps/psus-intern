# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit="res.partner"

    product_list_ids = fields.Many2one(comodel_name="product.list",
                                        string="Product List that this partner is using")
                                        #inverse_name="customer_ids")
                                        