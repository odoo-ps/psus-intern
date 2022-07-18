from odoo import fields, models


class ApiHeaderLines(models.Model):
    _name = 'api.header.lines'
    _description = "API Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    api_connection_id = fields.Many2one('api.connection', string='Headers')
