# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PartsPart(models.Model):
    _name = "parts.part"
    _description = "A component of a larger product."
    _order = "name"

    name = fields.Char(default=_("New"))
    #year = fields.Many2one("parts.year")
    #make = fields.Many2one("parts.make")
    #model = fields.Many2one("parts.model")
    #engine = fields.Many2one("parts.engine")
    #details = fields.Many2one("parts.details")
    year = fields.Char()
    make = fields.Char()
    model = fields.Char()
    engine = fields.Char()
    details = fields.Char()
