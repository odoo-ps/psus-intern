#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Sale(models.Model):
    _inherit = 'sale.order'

    