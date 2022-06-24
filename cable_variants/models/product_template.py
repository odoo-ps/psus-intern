# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _compute_default_code(self):
        super()._compute_default_code()
        for template in self.product_template_attribute_value_ids:
            print(template)
