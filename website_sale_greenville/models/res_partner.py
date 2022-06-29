from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_list_id = fields.Many2one(comodel_name='product.list',
         string='Product List')
