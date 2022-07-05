# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class model(models.Model):
    _name = "part"
    _description = "A component of a larger product."
    _order = "name"
