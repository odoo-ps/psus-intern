from operator import itemgetter
import requests

from odoo import api, models

class ApiRequest(models.Model):
    _name = "api.request"
    _description = "API Request"

    @api.model
    def get(self, api_config):
      url, params, headers = itemgetter('url', 'params', 'headers')(api_config)
      return requests.get(url, params=params, headers=headers)
        

    @api.model
    def post(self, api_config):
        url, params, headers, data = itemgetter('url', 'params', 'headers', 'local_payload')(api_config)
        try:
            response = requests.post(url, params=params, headers=headers, data=data)
            return response
        except requests.exceptions.ConnectionError:
            return "Failed connection try again or contact your API provider"
