# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Component(models.Model):
    _name = "component"
    _description = "A generic component and its information."

    name = fields.Char(string="Component")
    product_name = fields.Char(compute="_compute_product_name")
    brand_id = fields.Many2one("component.brand")
    model_id = fields.Many2one("component.model")
    version_id = fields.Many2one("component.version")
    internal_id = fields.Many2one("component.internal")
    external_id = fields.Many2one("component.external")

    @api.depends('brand_id', 'model_id', 'version_id',
                 'internal_id', 'external_id')
    def _compute_product_name(self):
        for component in self:
            new_name = "%s %s %s %s %s" % \
                        (component.version_id.name,
                         component.brand_id.name,
                         component.model_id.name,
                         component.internal_id.name,
                         component.external_id.name)
            component.product_name = new_name

    def action_search_show_wizard(self):
        component_ids = self.env['component'].browse(
            self._context.get('active_ids', False))
        lines = []

        for line in component_ids:
            vals = (0, 0, {
                'component_id': line.id
            })
            lines.append(vals)

        return {
            'name': _('Compatible Parts Available'),
            'type': 'ir.actions.act_window',
            'res_model': 'component.search.wizard',
            'target': 'new',
            'view_id':
                self.env.ref('filter.component_search_wizard_view_form').id,
            'view_mode': 'form',
            'context': {'default_search_line_ids': lines}
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
