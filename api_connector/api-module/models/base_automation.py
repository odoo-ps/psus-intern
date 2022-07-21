import json
import requests
import xml.etree.ElementTree as ET

from odoo import models


class BaseAutomation(models.Model):
    _inherit = 'base.automation'

    def test_api(self):
        action = self.action_server_id
        api_config = self._get_api_configuration(action)
        api_request = self.env['api.request']
        api_config['local_payload'] = json.dumps(action.xml2json(
            ET.XML(action._render_template_qweb(action.resource_ref)))) if action.is_xml(action.payload) else None
        method = api_config['method']
        api_response = requests.Response()
        try:
            if method == 'get':
                api_response = api_request.get(api_config)
            if method == 'post':
                api_response = api_request.post(api_config)  
        except Exception as e:
            print(type(e))
            if isinstance(e, requests.exceptions.ConnectionError) or isinstance(e, requests.exceptions.Timeout):
                api_response.raw = e
                api_response.status_code = 500
            if isinstance(e, requests.exceptions.MissingSchema):
                api_response.raw = e
                api_response.status_code = 400
        
        action._generate_log(method, api_config['url'], api_response)

    def _get_api_configuration(self, action):
        api_confg_fields = {
            'url': action.api_connection_id.url,
            'params': json.loads(action.json_params) or None,
            'method': action.api_connection_id.method,
            'headers': json.loads(action.translate_o2m(action.api_connection_id.header_ids)) or None,
        }
        return api_confg_fields
