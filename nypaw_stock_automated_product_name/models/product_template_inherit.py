# -*- coding: utf-8 -*-

import hashlib

from datetime import datetime
from odoo import api, fields, models


class ProductTemplateInherit(models.Model):

    _inherit = "product.template"

    gender = fields.Selection(
        string="Product Gender",
        selection=[
            ("gender1", "Gender 1"),
            ("gender2", "Gender 2"),
            ("gender3", "Gender 3"),
            ("gender4", "Gender 4"),
            ("gender5", "Gender 5"),
        ],
        default="gender1",
        required=True,
    )

    upc = fields.Char(string="Unique Product Code", store=True, readonly=True)

    def _calculate_hash(self, key):
        return hashlib.sha1(key.encode("utf-8")).hexdigest()

    @api.onchange("gender")
    def _compute_upc(self):

        self.init_gender_sequences()
        next_sequence = self.env["ir.sequence"].next_by_code(
            "product.template.gender." + self.gender
        )
        key = next_sequence + str(datetime.now())
        self.upc = self._calculate_hash(key)

    @api.onchange("categ_id")
    def _onchange_categ_id(self):
        def get_sequence_from_category_id(id):

            product_category = self.env["product.category"].search([("id", "=", id)])
            return product_category.sequence_id

        sequence = get_sequence_from_category_id(str(self.categ_id.id))
        if sequence:
            self.name = sequence.next_by_id()

    @api.model
    def init_gender_sequences(self):

        code = "product.template.gender.gender"

        for i in range(1, 6):
            temp_code = code + str(i)
            seq = self.env["ir.sequence"].search([("code", "=", temp_code)])
            if not seq:
                self.env["ir.sequence"].create(
                    {
                        "name": "Product Gender Sequence - " + str(i),
                        "code": temp_code,
                        "prefix": "GENDER" + str(i),
                        "padding": 6,
                    }
                )
