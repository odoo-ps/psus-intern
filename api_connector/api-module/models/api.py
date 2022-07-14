from odoo import fields, models


class Api(models.Model):
    _name = 'api'
    _description = 'API model'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    method = fields.Selection(
        selection=[('get', 'GET'), ('post', 'POST')],
        string='Method',
        required=True,
        default='get'
    )

    header_ids = fields.One2many(
        'api.header.lines', 'api_id', string='Headers')
    server_ids = fields.One2many(
        'ir.actions.server', 'api_id', string='Server Actions')


class ApiHeaderLines(models.Model):
    _name = 'api.header.lines'
    _description = "API Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    api_id = fields.Many2one('api', string='Headers')
