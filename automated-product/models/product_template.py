# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char(compute="_compute_name",
                       required=True)
    prefix_code = fields.Char(compute="_compute_prefix_code")
    order_reference = fields.Char(default=lambda self: _('xxxxxx'),
                                  readonly=True)
    product_gender = fields.Selection(
        string="Made For",
        selection=[('m', 'Adult Male'), ('f', 'Adult Female'),
                   ('u', 'Adult Unisex'), ('c', 'Child Unisex'),
                   ('n', 'None')],
        default='n',
        required=True,
        help="The gender the product is targetted or made for."
    )
    unique_upc = fields.Char(compute="_compute_unique_upc",
                             required=True, readonly=True)

    @api.depends('prefix_code', 'order_reference')
    def _compute_name(self):
        for record in self:
            new_name = record.prefix_code + record.order_reference
            if not record.name:
                record.name = new_name

    @api.depends('categ_id')
    def _compute_prefix_code(self):
        for record in self:
            # grab complete category information (id, string)
            # split category string
            # splice all subcategories to two letters, as list
            # join all prefixes with "/" and category id
            category = record.categ_id.name_get()[0]
            category = category[1].split(" / ")
            category = [cat[0:2] for cat in category]
            record.prefix_code = ("/".join(category)).upper() + \
                "/"

    @api.depends('product_gender', 'order_reference')
    def _compute_unique_upc(self):
        for record in self:
            prefix_gender = str(record.product_gender).upper()
            record.unique_upc = prefix_gender + record.order_reference

    # overwrite create function to make sequential reference number
    @api.model
    def create(self, vals):
        if vals.get('order_reference', _('xxxxxx')) == _('xxxxxx'):
            vals['order_reference'] = \
                (self.env['ir.sequence'].next_by_code(
                    'order.reference.template.seq') or _('xxxxxx'))
        res = super(ProductTemplate, self).create(vals)
        return res
