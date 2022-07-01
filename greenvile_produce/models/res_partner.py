from odoo import models,fields,api


class PartnerProductList(models.Model):
    _inherit='res.partner'

    products_to_purchase = fields.Many2one(comodel_name='greenvile.produce.productlist')

    