# -*- coding: utf-8 -*-

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def search(self, args, **kw):
        product_list_id = self.env.user.product_list_id
        if product_list_id:
            args = [('id', 'in', product_list_id.product_ids.ids), *args]
        return super().search(args, **kw)
