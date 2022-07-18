import json
import requests
import xml.etree.ElementTree as ET
from operator import attrgetter, itemgetter

from odoo import models
from odoo.exceptions import UserError


class BaseAutomation(models.Model):
    _inherit = 'base.automation'

    def test_api(self):
        action = self.action_server_id
        raw_headers = action.api_connection_id.header_ids or None
        params = json.loads(action.json_params) or None
        local_payload = json.dumps(action.xml2json(
            ET.XML(action._render_template_qweb(action.resource_ref)))) if action.is_xml(action.payload) else None
        
        method = action.api_connection_id.method
        headers = json.loads(action.translate_o2m(
            raw_headers)) if raw_headers else None
        api_response = None
        try:
            if method == 'get':
                api_response = requests.get(
                    action.api_connection_id.url, headers=headers, params=params)
            else:
                api_response = requests.post(
                    action.api_connection_id.url, headers=headers, data=local_payload)  
        except Exception:
            raise UserError(
                "Something went wrong please retry or check the logs")

        self.env['log.lines'].create({
            'call': "%s %s" % (method, action.api_connection_id.url),
            'response': api_response.text,
            'server_id': action.id,
            'status':  api_response.status_code,
        })
        if api_response.status_code >= 400:
            print("Error: -> %s" % api_response.text)
