# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class FilterWizard(models.TransientModel):
    _name = "filter.wizard"
    _description = "Handles the search actions for the filter."

    parts_id = fields.Many2one("parts.part", required=True)

    def action_search(self):
        ctx = dict(self.env.context)
        ctx.update({
            'search_default_year_id': self.parts_id.year_id
        })
        return {
            'name': _('Returned Search'),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'filter_wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': ctx
        }
