# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"


class ProductCategory(models.Model):
    _inherit = "product.category"

    # TODO: autogenerate name based on selected product categories
    # follow Odoo name nomenclature
