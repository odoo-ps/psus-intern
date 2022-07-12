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

        errors = {
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            408: "Request Timeout",
            500: "Internal Server Error",
            502: "Bad Gateway",
            503: "Service Unavailable",
            511: "Network Authentication Required",
        }

        if not url or not method:
            raise UserError('API must have a url and method')

        try:
            if method == 'get':
                response = requests.get(url, headers=headers, params=params)
            else:
                response = requests.post(url, headers=headers, data=payload)
            
            if response.status_code >= 200 and response.status_code < 400:
                action.response = response.text
            elif response.status_code in errors:
                action.response = response.text
                raise UserError(
                    errors[response.status_code] + " -> " + response.text)
            else:
                action.response = response.text
                raise Exception("Unknow Error ->" + response.text)
                
        except Exception as e:
            action.response = response.text
            raise UserError(
                "Something went wrong please retry or check the logs")
