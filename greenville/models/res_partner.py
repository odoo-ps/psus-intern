# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit="res.partner"

    #which product list this customer is using
    product_list_id = fields.Many2one(comodel_name="product.list",
                                        string="Using Product List")
                                        #inverse_name="customer_ids")
    