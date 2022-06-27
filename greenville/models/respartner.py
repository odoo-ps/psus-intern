# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class resPartner (models.Model):
    _inherit = 'res.partner'

    
    list_ids = fields.Many2one(comodel_name='productlist', string='Product lists',)
