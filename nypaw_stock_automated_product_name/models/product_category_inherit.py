# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProductCategoryInherit(models.Model):

    _inherit = "product.category"

    sequence_id = fields.Many2one(
        comodel_name="ir.sequence", string="Sequence", required=True, readonly=True
    )

    @api.model
    def create(self, vals):
        print("Inside inherited product category method ***************** ", vals)
        sequence = self.env["ir.sequence"].create(
            {
                "name": vals["name"],
                "code": "product.category.sequence_id." + vals["name"],
                "prefix": vals["name"].upper().replace(" ", ""),
            }
        )
        vals["sequence_id"] = sequence.id
        return super(ProductCategoryInherit, self).create(vals)
