# -*- coding: utf-8 -*-

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def search(self, args, **kwargs):
        if self.env.user.product_list_id:
            args.append(('id', 'in', self.env.user.product_list_id.product_ids.ids))

        return super().search(args, **kwargs)