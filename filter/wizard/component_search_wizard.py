# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ComponentSearchWizard(models.TransientModel):
    _name = "component.search.wizard"
    _description = "Handles the component search"

    def _get_default_components(self):
        return self.env['component'].browse(self.env.context.get('active_id'))

    component_ids = fields.Many2many('component',
                                     default=_get_default_components)
    search_line_ids = fields.One2many(
        'component.search.wizard.line', 'search_id',
        string="Available Components")

    def action_search(self):
        print("wizard: ", self.component_ids)

        return True
        # this is reached
