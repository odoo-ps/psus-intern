# -*- coding:utf-8 -*-


from odoo import models, fields, api


class product_to_customer_mapping(models.Model):
    _inherit = 'res.partner'

    product_list_to_customers = fields.Many2one('greenville.productlist', string='Customers using this product list')