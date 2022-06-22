#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    pair_per_case = fields.Integer(string="pair_per_case")
    price_per_pair = fields.Monetary(string="price_per_pair")
    
    state = fields.Selection([('editable', 'Editable'), ('read_only',
                              'Read Only')], 'Status', copy=False, default='editable', readonly=True)

    list_price = fields.Float(compute='_compute_list_price',
                              inverse='_inverse_list_price',
                              store=True,
                              states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]})
    
    
    
    @api.onchange('pair_per_case',"price_per_pair")
    def _onchange_(self):
        self.ensure_one()
        if self.pair_per_case != 0 and self.price_per_pair != 0:
            self.list_price = self.pair_per_case*self.price_per_pair
            self.state='read_only'
        else:
            self.state='editable'
