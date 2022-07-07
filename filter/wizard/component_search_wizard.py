# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class ComponentSearchWizard(models.TransientModel):
    _name = "component.search.wizard"
    _description = "Component Search Wizard"

    # wizard related information
    name = fields.Char(default=lambda self: _('New'))
    component_ids = fields.Many2many("component")
    is_completed = fields.Boolean(default=False)

    # the selected options
    brand_id = fields.Many2one("component.brand", required=True)
    model_id = fields.Many2one("component.model", required=True)
    version_id = fields.Many2one("component.version", required=True)
    internal_id = fields.Many2one("component.internal", required=True)
    external_id = fields.Many2one("component.external", required=True)

    def action_search_wizard(self):
        self.name = "Available Components for %s %s %s %s %s" % \
            (self.version_id.name, self.brand_id.name,
             self.model_id.name, self.internal_id.name,
             self.external_id.name)
        self.is_completed = True

        self.component_ids = self.env['component'].search([
            ('brand_id', '=', self.brand_id.id),
            ('model_id', '=', self.model_id.id),
            ('version_id', '=', self.version_id.id),
            ('internal_id', '=', self.internal_id.id),
            ('external_id', '=', self.external_id.id)
        ])

        # find way to show results of search
        return True
