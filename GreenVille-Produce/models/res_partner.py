# -*- coding:utf-8 -*-


from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'

    product_list_to_customers = fields.Many2one('product.list', string='Customers using this product list')