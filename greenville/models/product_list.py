# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductList(models.Model):
    _name = "product.list"
    _description = "Product List"

    name = fields.Char(string="Title",required=True)

    """
    product_ids = fields.Many2many(comodel_name="product.product",
                                    string="Products on this List")
                                    #inverse_name="product_list_ids")"""

    #products that are on this list
    product_ids = fields.Many2many(comodel_name="product.template",
                                    string="Products on this list")

    

    """customer_ids = fields.One2many(comodel_name="res.partner",
                                    string="Customers using this List",
                                    inverse_name="product_list_ids")"""

    #customers who are using this list
    customer_ids = fields.One2many(comodel_name="res.partner",inverse_name="product_list_id",string="Customers using list")

    """
    current_user = fields.Many2one('res.users',compute='_get_current_user')

    @api.depends()
    def _get_current_user(self):
        for record in self:
            record.current_user = self.env.user
            """