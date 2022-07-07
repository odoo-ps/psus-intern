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
