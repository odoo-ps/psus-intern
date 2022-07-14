import json
import requests
import xml.etree.ElementTree as ET


from odoo import models
from odoo.exceptions import UserError


class BaseAutomation(models.Model):
    _inherit = 'base.automation'

    def test_api(self):
        action = self.env['ir.actions.server'].search(
            [('state', '=', 'api_call'), ('id', '=', self.action_server_id.id)])
        raw_headers = action.api_id.header_ids or None
        params = json.loads(action.json_params) or None
        local_payload = None if not action.payload else json.dumps(action.xml2json(
            ET.XML(action._render_template_qweb(action.resource_ref))))
        url = action.api_id.url
        method = action.api_id.method
        headers = json.loads(self.env['ir.actions.server'].translate_o2m(
            raw_headers)) if raw_headers else None
        api_response = None
        try:
            if method == 'get':
                api_response = requests.get(
                    url, headers=headers, params=params)
            else:
                api_response = requests.post(
                    url, headers=headers, data=local_payload)  
        except Exception:
            raise UserError(
                "Something went wrong please retry or check the logs")

        self.env['log.lines'].create({
            'call': "%s %s" % (method, url),
            'response': api_response.text,
            'server_id': action.id,
            'status':  api_response.status_code,
        })
        if api_response.status_code >= 400:
            raise UserError("Error: -> %s" % api_response.text)
