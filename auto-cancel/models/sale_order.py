# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _description = """Information about a sale order."""
    _inherit = "sale.order"

    validity = fields.Integer()
