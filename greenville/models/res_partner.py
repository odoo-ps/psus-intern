# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = "res.partner"

    product_list = fields.Many2one('custom.products', ondelete='set null')