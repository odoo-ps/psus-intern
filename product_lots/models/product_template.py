# -*- coding: utf-8 -*-
from email.policy import default
from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_number_prefix = fields.Char(string='Lot Number Prefix', default="00")
    lot_number = fields.Char(string='Lot Number', compute="_compute_lot_number", store="True")
    sequence = fields.Char(string='Sequence', store="False",  default=lambda self: self.env['ir.sequence'].with_context(lot_number_prefix=self.lot_number_prefix).next_by_code('product.template'))

    @api.depends('lot_number_prefix')
    def _compute_lot_number(self):
        for record in self:
            print(type(record.lot_number_prefix), type(record.sequence))
            print(record.lot_number_prefix, record.sequence)
            record.lot_number = record.lot_number_prefix + str(record.sequence)

    
