# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection(
        string='Customer Type',
        selection=[('patient', 'patient'),
                   ('caregiver', 'caregiver'),
                   ('external_patient', 'external_patient'),
                   ('customer', 'customer')]
    )
