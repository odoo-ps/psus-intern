# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #add type selection field
    customer_type = fields.Selection(string='Custumer Type', 
                               selection=[('consumer', 'Consumer'),
                                          ('patient', 'Patient'),
                                          ('caregiver', 'Caregiver'),
                                          ('externalpatient', 'ExternalPatient')])
