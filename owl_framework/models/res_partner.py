# -- coding: utf-8 --"
from odoo import api, fields, models

class ResPartner(models.Model):
  _inherit = 'res.partner'

  costumer_type = fields.Selection(
    string='customer_type',
    selection=[('patient','Patient'),
    ('caregiver','Caregiver'),
    ('externalpatient','ExternalPatient'),
    ('consumer','Consumer')],
    copy=False
  )
