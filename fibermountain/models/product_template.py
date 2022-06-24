#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductAttribute(models.Model):
    _inherit = "product.attribute.value"
    
    code = fields.Char(string="code")
    
   