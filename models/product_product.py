# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def search(self, args, **kwargs):
        product_list_id = self.env.user.product_list_id
        
        if product_list_id:
            args = [('id', 'in', product_list_id.product_ids.ids), *args]
        
        return super().search(args, **kwargs)
