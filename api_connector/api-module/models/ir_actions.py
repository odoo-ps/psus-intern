from collections import defaultdict
from lxml import html
import json
import requests
import xml.etree.ElementTree as ET

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    state = fields.Selection(selection_add=[(
        'api_call', 'Call External API')], ondelete={'api_call': 'cascade'})
    api_id = fields.Many2one('api', string='API')
    params_ids = fields.One2many(
        'ir.actions.server.params.lines', 'server_id', string='Params')
    json_params = fields.Text(
        string='JSON Params', compute='_compute_json_params', default='{}', store=True, readonly=True)
    response = fields.Text(string='Response', readonly=True)
    payload = fields.Text(string='Payload')
    log_ids = fields.One2many('log.lines', 'server_id', readonly=True)

    def _run_action_api_call(self, eval_context=None):
        self.ensure_one()
        params = json.loads(self.json_params) or None
        print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA {ET.XML(str(self._render_template_qweb()))}")
        lpayload = self.xml2json(ET.XML(self._render_template_qweb())) or None

        url = self.api_id.url
        method = self.api_id.method
        headers = json.loads(self.translate_o2m(
            self.api_id.header_ids)) or None
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
                api_response = requests.get(url, headers=headers, params=params)
                self.env['log.lines'].create({
                    'call': f"{method} {url}",
                    'response': api_response,
                    'server_id': self.id,
                    'status':  api_response.status_code,

                })
            if method == 'post':
                print(lpayload)
                print(type(lpayload))
                api_response = requests.post(url, headers=headers, data=json.dumps(lpayload))

            if api_response.status_code >= 200 and api_response.status_code < 400:
                # self.response = response.text
                print(api_response.json())
            elif api_response.status_code in errors:
                self.response = api_response.text
                raise UserError(
                    errors[api_response.status_code] + " -> " + api_response.text)
            else:
                self.response = api_response.text
                raise Exception("Unknow Error ->" + api_response.text)

        except Exception as e:
            self.response = api_response.text
            raise UserError(
                "Something went wrong please retry or check the logs")

    @api.depends('params_ids')
    def _compute_json_params(self):
        for server in self:
            server.json_params = server.translate_o2m(server.params_ids)

    def translate_o2m(self, one2many_field):
        json_field = {line.key: line.value for line in one2many_field}
        return json.dumps(json_field)

    def _render_template_qweb(self):
        try:
            model = self.model_id.model
            values = {
                'object': self.env[model].search([('id', "=", self._context.get('active_id', False))]),
            }
            render_result = self.env['ir.qweb']._render(
                html.fragment_fromstring(self.payload), values)
        except Exception as e:
            raise UserError(("Failed to render QWeb template : %s)", e))
        return render_result

    def xml2json(self, t):
        d = {t.tag: {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(self.xml2json, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k: v[0] if len(v) == 1 else v
                         for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update(('@' + k, v)
                            for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    d[t.tag]['#text'] = text
            else:
                d[t.tag] = text
        return d


class IrActionsServerParamsLines(models.Model):
    _name = 'ir.actions.server.params.lines'
    _description = "Actions Server Params O2M Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    server_id = fields.Many2one('ir.actions.server', string='API')
    
    
class LogLines(models.Model):
    _name = 'log.lines'
    _description = 'API logs'

    log_id = fields.Many2one('logs', string='API')
    server_id = fields.Many2one('ir.actions.server', string='API')
    call = fields.Char(string='Call')
    response = fields.Text(string='Response')
    status = fields.Char(string='Status')
    
    
