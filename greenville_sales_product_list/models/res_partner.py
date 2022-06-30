# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    product_list_id = fields.Many2one(comodel_name="product.list")
    available_tag_ids = fields.Many2many(related="product_list_id.tag_ids")
