# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection(
        string='Customer Type',
        selection=[('patient', 'Patient'),
                   ('caregiver', 'Caregiver'),
                   ('external_patient', 'External Patient'),
                   ('customer', 'Customer')]
    )
