# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    product_list_id=fields.Many2one(comodel_name="greenville.products.list", string="Product List")