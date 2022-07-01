# -*- coding: utf-8 -*-

from odoo import fields,api,models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    plant_code = fields.Text(string="Plant Code")

