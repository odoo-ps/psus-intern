import json
import requests

from odoo import api, fields, models
from odoo.exceptions import UserError


class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    state = fields.Selection(selection_add=[(
        'api_call', 'Call External API')], ondelete={'api_call': 'cascade'})

    api_id = fields.Many2one('api', string='API')

    payload_ids = fields.One2many(
        'ir.actions.server.payload.lines', 'server_id', string='Payload')

    params_ids = fields.One2many(
        'ir.actions.server.params.lines', 'server_id', string='Params')

    json_payload = fields.Text(
        string='JSON Payload', compute='_compute_json_payload', default='{}', store=True, readonly=True)

    json_params = fields.Text(
        string='JSON Params', compute='_compute_json_params', default='{}', store=True, readonly=True)

    response = fields.Text(string='Response', readonly=True)

    def _run_action_api_call(self, eval_context=None):
        self.ensure_one()
        params = json.loads(self.json_params) or None
        payload = json.loads(self.json_payload) or None

        url = self.api_id.url
        method = self.api_id.method
        headers = json.loads(self.translate_o2m(
            self.api_id.header_ids)) or None

        if not url or not method:
            raise UserError('API must have a url and method')

        try:
            if method == 'get':
                response = requests.get(url, params=params, headers=headers)
                self.response = response.text
        except Exception as e:
            raise UserError(e)

    @api.depends('payload_ids')
    def _compute_json_payload(self):
        for server in self:
            server.json_payload = server.translate_o2m(server.payload_ids)

    @api.depends('params_ids')
    def _compute_json_params(self):
        for server in self:
            server.json_params = server.translate_o2m(server.params_ids)

    def translate_o2m(self, one2many_field):
        json_field = {line.key: line.value for line in one2many_field}
        return json.dumps(json_field)


class IrActionsServerPayloadLines(models.Model):
    _name = 'ir.actions.server.payload.lines'
    _description = "Actions Server Payload O2M Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    server_id = fields.Many2one('ir.actions.server', string='API')


class IrActionsServerParamsLines(models.Model):
    _name = 'ir.actions.server.params.lines'
    _description = "Actions Server Params O2M Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    server_id = fields.Many2one('ir.actions.server', string='API')
