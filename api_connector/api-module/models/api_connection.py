from odoo import fields, models


class ApiConnection(models.Model):
    _name = 'api.connection'
    _description = 'API model'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    method = fields.Selection(
        selection=[('get', 'GET'), ('post', 'POST')],
        string='Method',
        default='get',
        required = True
    )

    header_ids = fields.One2many(
        'api.header.lines', 'api_connection_id', string='Headers')
    server_ids = fields.One2many(
        'ir.actions.server', 'api_connection_id', string='Server Actions')



