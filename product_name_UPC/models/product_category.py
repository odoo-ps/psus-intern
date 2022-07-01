from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    category_sequence_id = fields.Many2one(
        "ir.sequence", ondelete='cascade', required=True)
