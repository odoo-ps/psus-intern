# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection(string="Customer Type", selection=[
        ('consumer', 'Consumer'),
        ('patient', 'Patient'),
        ('caregiver', 'Caregiver'),
        ('external_patient', 'ExternalPatient')
        ])
