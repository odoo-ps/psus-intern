from operator import itemgetter
import requests

from odoo import api, models

class ApiRequest(models.Model):
    _name = "api.request"
    _description = "API Request"

    @api.model
    def get(self, api_config):
        url, params, headers = itemgetter('url', 'params', 'headers')(api_config)
        return requests.get(url, params=params, headers=headers, timeout=10)
        
    @api.model
    def post(self, api_config):
        url, params, headers, local_payload = itemgetter('url','params', 'headers', 'local_payload')(api_config)
        response = requests.post(url, params=params, headers=headers, data=local_payload)
        return response

    @api.model
    def put(self, api_config):
        url, params, headers, local_payload = itemgetter('url', 'params', 'headers', 'local_payload')(api_config)
        url = self._format_url(url, params)
        response = requests.put(url, headers=headers, data=local_payload)
        return response

    @api.model
    def patch(self, api_config):
        url, params, headers, local_payload = itemgetter('url', 'params', 'headers', 'local_payload')(api_config)
        url = self._format_url(url, params)
        response = requests.patch(url, headers=headers, data=local_payload)
        return response

    @api.model
    def delete(self, api_config):
        url, params, headers = itemgetter('url', 'params', 'headers')(api_config)
        url = self._format_url(url, params) if params else url
        response = requests.delete(url, headers=headers)
        return response

    def _format_url(self, url, params):
        if url.endswith('/'):
            url = url[:-1]
        for key in params:
            url = url + '/%s' % params[key]
        return url
