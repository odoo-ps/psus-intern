# coding: utf-8 
from odoo import api,fields,models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  lot_number_prefix = fields.Char(string="Lot's prefix")
