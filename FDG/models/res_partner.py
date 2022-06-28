# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResPartner(models.Model):
  _inherit = "res.partner"

  is_sales_person = fields.Boolean(
    string="Is sales person",
    compute="_compute_is_sale_person"
  )

  def _compute_is_sale_person(self):
    if self.env.user.has_group('sales_team.group_sale_manager'):
      self.is_sales_person = False
      return
    if self.env.user.has_group('sales_team.group_sale_salesman') or self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
      self.is_sales_person = True
