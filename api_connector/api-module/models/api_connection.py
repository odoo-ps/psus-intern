import json

from odoo import api,fields, models


class ApiConnection(models.Model):
    _name = 'api.connection'
    _description = 'API model'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    method = fields.Selection(
        selection=[('get', 'GET'), ('post', 'POST'),('put','PUT'),('patch','PATCH'),('delete','DELETE')],
        string='Method',
        default='get'
    )

    header_ids = fields.One2many(
        'api.header.lines', 'api_connection_id', string='Headers')
    server_ids = fields.One2many(
        'ir.actions.server', 'api_connection_id', string='Server Actions')

    json_headers = fields.Text(string='JSON Headers', compute='_compute_json_headers', readonly=True, store=True)

    @api.depends('header_ids')
    def _compute_json_headers(self):
        for api_connection in self:
            api_connection.json_headers = self.env['ir.actions.server'].translate_o2m(self.header_ids)
            
