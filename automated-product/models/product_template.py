# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # name will be generated upon creation of product
    name = fields.Char()

    product_gender = fields.Selection(
        string="Made For",
        selection=[('male', 'Adult Male'), ('female', 'Adult Female'),
                   ('unisex', 'Adult Unisex'), ('child', 'Child Unisex'),
                   ('none', 'None')],
        default='none',
        required=True,
        help="The gender the product is targetted or made for."
    )
    unique_upc = fields.Char(default="Nxxxxxx",
                             compute="_compute_unique_upc",
                             store=True, readonly=True)

    @api.depends('product_gender')
    def _compute_unique_upc(self):
        # TODO: self.categ_id.product_count counts all products
        # find way to only count products in same category as current product
        digits = str("0" * (6 - len(str(self.categ_id.product_count))))
        signifier = "X"
        match self.product_gender:
            case 'male':
                signifier = "M"
            case 'female':
                signifier = "F"
            case 'unisex':
                signifier = "U"
            case 'child':
                signifier = "C"
            case 'none':
                signifier = "N"
        self.unique_upc = signifier + digits + str(self.categ_id.product_count)
