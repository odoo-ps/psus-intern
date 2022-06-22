# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ProductTemplate(models.Model):
  _inherit = "product.template"

  pair_per_case = fields.Integer(string="Number of pairs")

  price_per_pair = fields.Monetary(string="Price of pair")
  list_price = fields.Float(
    compute='_compute_list_price',
    store=True,
    default=None
  )
  
  @api.onchange('pair_per_case',"price_per_pair")
  def _onchange_calculate_price_list(self):
    self.ensure_one()
    if self.pair_per_case and self.price_per_pair:
      self.list_price = self.pair_per_case * self.price_per_pair
