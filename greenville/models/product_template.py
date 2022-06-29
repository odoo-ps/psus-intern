# -*- coding: utf-8 -*-
'''
from odoo import models, fields, api


class ProductTemplate(models.Model):
    #_name="product.product"
    _inherit="product.template"

    current_user = fields.Many2one('res.users',compute='_get_current_user')

    """
    product_list_ids = fields.Many2one(comodel_name="res.partner",
                                        string="In Product List",
                                        related="product_list_ids")
                                        #inverse_name="customer_ids")
                                        """

    product_list_ids = fields.Many2many(comodel_name="product.list",
                                        string="Lists that this Product appears in")

    @api.depends()
    def _get_current_user(self):
        for record in self:
            record.current_user = self.env.user

    def get_list(self):
        for record in self:
            if record.product_list_ids: #if is set (there is a list)
                if self.env.user in record.product_list_ids.customer_ids:
                    return True
'''