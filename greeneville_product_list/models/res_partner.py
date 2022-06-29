# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    product_list_id = fields.Many2one(comodel_name='product.list',
                                      string='Product List')

    product_categ_ids = fields.Many2many(comodel_name='product.category',
                                         string='Available Product Categories',
                                         compute='_compute_product_categ_ids',
                                         store=True)

    @api.depends('product_list_id')
    def _compute_product_categ_ids(self):
        for record in self:
            for product_id in record.product_list_id.product_ids:
                if product_id and product_id.categ_id:
                    record.product_categ_ids = [(4, product_id.categ_id.id)]
