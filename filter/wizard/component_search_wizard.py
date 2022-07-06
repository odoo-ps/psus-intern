# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ComponentSearchWizard(models.TransientModel):
    _name = "component.search.wizard"
    _description = "Handles the component search"

    search_line_ids = fields.One2many(
        'component.search.wizard.line', 'search_id',
        string="Available Components")

    def action_search(self):
        print("its doing something")
        return True
        # do something
