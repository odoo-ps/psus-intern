# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ComponentSearchWizardLine(models.TransientModel):
    _name = "component.search.wizard.line"
    _description = "Searched Components"

    search_id = fields.Many2one("component.search.wizard")
    component_id = fields.Many2one("component")
