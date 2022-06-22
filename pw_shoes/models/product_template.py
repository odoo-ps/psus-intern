# -- coding: utf-8 --

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pair_per_case = fields.Integer(string='Pairs per case')
    price_per_pair = fields.Float(string='Price per pair')

    list_price = fields.Float(string='Sales price', compute='_compute_list_price',
                              readonly=True,
                              store=True,
                              states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]})
    state = fields.Selection([('editable', 'Editable'), ('read_only',
                                                         'Read Only')], 'Status', copy=False, default='editable')

    @api.depends('price_per_pair', 'pair_per_case')
    def _compute_list_price(self):
        self.ensure_one()
        if(self.price_per_pair < 0 or self.pair_per_case < 0):
            raise ValidationError(
                ('Price per pair and pair per case must be positive'))
        elif(self.price_per_pair == 0 and self.pair_per_case == 0):
            self.state = 'editable'
        else:
            self.state = 'read_only'
            self.list_price = self.price_per_pair *  self.pair_per_case
