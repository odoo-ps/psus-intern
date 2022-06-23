from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    customer_type = fields.Selection(string='Customer Type',
                                     selection=[('consumer', 'Consumer'),
                                                ('patient', 'Patient'),
                                                ('caregiver', 'Caregiver'),
                                                ('externalpatient', 'ExternalPatient')])
