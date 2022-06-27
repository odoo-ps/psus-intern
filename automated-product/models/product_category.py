# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    # inherits parent_id (houses product category)
    # but sets it as required
    parent_id = fields.Many2one(required=True)
