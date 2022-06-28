import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    product_list = fields.Many2one("product.lists", string="Customer Using List")


class ProductLists(models.Model):
    _name = "product.lists"
    _description = "New model product lists"
    name = fields.Char("Product List")
    products = fields.Many2many("product.product")

    customers_using_this_list = fields.One2many(
        "res.partner", "product_list", string="Customer Using List"
    )
    tag = fields.Many2many("res.partner")

    @api.model
    def create(self, vals):
        return super().create(vals)
