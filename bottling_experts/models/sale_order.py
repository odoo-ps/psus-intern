from odoo import fields, models

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  travel_in = fields.Date(string="Travel In")
  travel_out = fields.Date(string="Travel Out")

  opportunity_name = fields.Char(string="Opportunity name")
