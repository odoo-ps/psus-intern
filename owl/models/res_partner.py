# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    costumer_type=fields.Selection(string='Costumer Type', 
    selection=[('consumer', 'Consumer'), ('patient', 'Patient'), ('caregiver', 'Caregiver'), ('externalPatient', 'External patient?')])
