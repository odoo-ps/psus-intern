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
