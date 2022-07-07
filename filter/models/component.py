# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Component(models.Model):
    _name = "component"
    _description = "A generic component and its information."

    name = fields.Char(string="Component")
    brand_id = fields.Many2one("component.brand")
    model_id = fields.Many2one("component.model")
    version_id = fields.Many2one("component.version")
    internal_id = fields.Many2one("component.internal")
    external_id = fields.Many2one("component.external")

    def action_search_show_wizard(self):
        component_ids = self.env['component'].browse(self.env.context.get('active_id'))

        # doesnt exist
        print("main: ", component_ids)

        return {
            'name': _('Compatible Parts Available'),
            'type': 'ir.actions.act_window',
            'res_model': 'component.search.wizard',
            'target': 'new',
            'view_id':
                self.env.ref('filter.component_search_wizard_view_form').id,
            'view_mode': 'form',
            'context': {'default_component_ids': component_ids}
        }


class ComponentBrand(models.Model):
    _name = "component.brand"
    _description = "Brand name of a Component"
    _order = "name"

    name = fields.Char()
    component_ids = fields.One2many("component", "brand_id")


class ComponentModel(models.Model):
    _name = "component.model"
    _description = "Model name of a Component"
    _order = "name"

    name = fields.Char()
    component_ids = fields.One2many("component", "model_id")


class ComponentVersion(models.Model):
    _name = "component.version"
    _description = "Version number of a Component"
    _order = "name"

    name = fields.Char()
    component_ids = fields.One2many("component", "version_id")


class ComponentInternal(models.Model):
    _name = "component.internal"
    _description = "Internal specifications of a Component"
    _order = "name"

    name = fields.Char()
    component_ids = fields.One2many("component", "internal_id")


class ComponentExternal(models.Model):
    _name = "component.external"
    _description = "External specifications of a Component"
    _order = "name"

    name = fields.Char()
    component_ids = fields.One2many("component", "external_id")
