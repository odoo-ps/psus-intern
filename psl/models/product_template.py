# coding: utf-8 

from odoo import fields,models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  lot_number_prefix = fields.Char(string="Lot NUmber Prefix")
