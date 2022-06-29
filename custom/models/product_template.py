# -*- coding:utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'
