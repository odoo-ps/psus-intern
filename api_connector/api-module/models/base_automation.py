import json
import requests
import xml.etree.ElementTree as ET

import pdb

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
        type_of_requests = {
            'get': api_request.get,
            'post': api_request.post,
            'put': api_request.put,
            'patch': api_request.patch,
            'delete': api_request.delete,
        }
        try:
            api_response = type_of_requests[method](api_config)
        except requests.exceptions.MissingSchema as e:
            api_response.status_code = 400
            api_response.raw = e
        except requests.exceptions.Timeout as e:
            api_response.status_code = 408
            api_response.raw = e
        except requests.exceptions.ConnectionError as e:
            api_response.status_code = 500
            api_response.raw = e
        
        action._generate_log(method, api_config['url'], api_response)
    
    def _get_api_configuration(self, action):
        api_confg_fields = {
            'url': action.api_connection_id.url,
            'params': json.loads(action.json_params) or None,
            'method': action.api_connection_id.method,
            'headers': json.loads(action.translate_o2m(action.api_connection_id.header_ids)) or None,
        }
        return api_confg_fields
