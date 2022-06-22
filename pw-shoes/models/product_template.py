# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ProductTemplate(models.Model):
  _inherit = "product.template"

  pair_per_case = fields.Integer(string="pair_per_case")

  price_per_pair = fields.Monetary(string="price_per_pair")
  
  state = fields.Selection([('editable', 'Editable'), ('read_only',
                            'Read Only')], 'Status', copy=False, default='editable',readonly=True)
  
  list_price = fields.Float(
    compute='_compute_list_price',
    inverse='_inverse_list_price',
    store=True,
    states={'editable': [('readonly', False)], 'read_only': [('readonly', True)]}
  )
  
  @api.onchange('pair_per_case',"price_per_pair")
  def calculate_price_list(self):
    self.ensure_one()
    if self.pair_per_case and self.price_per_pair:
       self.list_price = self.pair_per_case * self.price_per_pair
       self.state='read_only'
