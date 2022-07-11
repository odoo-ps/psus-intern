import json
import requests

from odoo import models
from odoo.exceptions import UserError


class BaseAutomation(models.Model):
    _inherit = 'base.automation'

    def test_api(self):
        action = self.env['ir.actions.server'].search(
            [('state', '=', 'api_call'), ('id', '=', self.action_server_id.id)])
        raw_headers = action.api_id.header_ids or None
        params = json.loads(action.json_params) or None
        payload = action.json_payload or None

        url = action.api_id.url
        method = action.api_id.method
        headers = self.env['ir.actions.server'].translate_o2m(
            raw_headers) if raw_headers else None

        if not url or not method:
            raise UserError('API must have a url and method')
        try:
            if method == 'get':
                response = requests.get(url, params=params)
                action.response = response.text
        except Exception as e:
            raise UserError(e)
