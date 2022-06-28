# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection([
        ('consumer', 'Consumer'),
        ('patient', 'Patient'),
        ('caregiver', 'Caregiver'),
        ('external_patient', 'External Patient'),
    ], string='Customer Type', required=True, default='consumer')
