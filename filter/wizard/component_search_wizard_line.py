# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ComponentSearchWizardLine(models.TransientModel):
    _name = "component.search.wizard.line"
    _description = "Searched Components"

    search_id = fields.Many2one("component.search.wizard")

    brand_id = fields.Many2one("component.brand")
    model_id = fields.Many2one("component.model")
    version_id = fields.Many2one("component.version")
    internal_id = fields.Many2one("component.internal")
    external_id = fields.Many2one("component.external")
