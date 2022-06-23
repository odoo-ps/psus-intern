from odoo import api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    customer_type_id = fields.Selection([('consumer','Consumer'),
        ('patient','Patient'),
        ('caregiver','Caregiver'),
        ('externalpatient','ExternalPatient')])
