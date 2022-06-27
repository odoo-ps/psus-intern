# -*- coding: utf-8 -*-"
from odoo import api, fields, models

class ResPartner(models.Model):
  _inherit = 'res.partner'

  costumer_type = fields.Selection(
    string='Costumer Type',
    selection=[
      ('patient','Patient'),
      ('caregiver','Caregiver'),
      ('externalpatient','External Patient'),
      ('consumer','Consumer')
    ]
  )
