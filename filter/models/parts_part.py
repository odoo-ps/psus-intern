# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class PartsPart(models.Model):
    _name = "parts.part"
    _description = "A component of a larger product."
    _order = "name"

    name = fields.Char(default=_("New"))
    year_id = fields.Many2one("parts.year", string="Year")
    make_id = fields.Many2one("parts.make", string="Make")
    model_id = fields.Many2one("parts.model", string="Model")
    engine_id = fields.Many2one("parts.engine", string="Engine")
    details_id = fields.Many2one("parts.details", string="Details")
    status = fields.Selection(
        string='Status',
        default='available',
        required=True,
        help='Check if product is currently available or offered.',
        selection=[('available', 'Available'), ('unavailable', 'No Stock')])

    def action_search(self):
        ctx = dict(self.env.context)
        ctx.update({
            'search_default_year_id': self.parts_id.year_id
        })
        return {
            'name': _('Returned Search'),
            'res_model': 'filter.wizard',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': ctx
        }


class PartsYear(models.Model):
    _name = "parts.year"
    _description = "Year Made"

    name = fields.Char(string="Year", required=True)
    part_ids = fields.One2many("parts.part", "year_id")


class PartsMake(models.Model):
    _name = "parts.make"
    _description = "Brand"

    name = fields.Char(required=True)
    part_ids = fields.One2many("parts.part", "make_id")


class PartsModel(models.Model):
    _name = "parts.model"
    _description = "Model"

    name = fields.Char(required=True)
    part_ids = fields.One2many("parts.part", "model_id")


class PartsEngine(models.Model):
    _name = "parts.engine"
    _description = "Engine Model"

    name = fields.Char(required=True)
    part_ids = fields.One2many("parts.part", "engine_id")


class PartsDetails(models.Model):
    _name = "parts.details"
    _description = "Trim Level"

    name = fields.Char(required=True)
    part_ids = fields.One2many("parts.part", "details_id")
