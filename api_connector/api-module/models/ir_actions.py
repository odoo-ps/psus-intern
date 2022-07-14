from collections import defaultdict
from lxml import html
import json
import requests
import xml.etree.ElementTree as ET

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    @api.model
    def _selection_target_model(self):
        return [(model.model, model.name)
                for model in self.env['ir.model'].search([])]

    @api.model
    def default_get(self, fields):
        result = super(IrActionsServer, self).default_get(fields)
        if not result.get('id') or 'resource_ref' not in fields:
            return result
        ir_actions_server = self.env['ir.actions.server'].browse(
            result['id'])
        res = self.env[ir_actions_server.model_id.model].search([], limit=1)
        if res:
            result['resource_ref'] = '%s,%s' % (
                ir_actions_server.model_id.model, res.id)
        return result

    state = fields.Selection(selection_add=[(
        'api_call', 'Call External API')], ondelete={'api_call': 'cascade'})
    api_id = fields.Many2one('api', string='API')
    resource_ref = fields.Reference(
        string='Record for testing', selection='_selection_target_model')

    params_ids = fields.One2many(
        'ir.actions.server.params.lines', 'server_id', string='Params')
    json_params = fields.Text(
        string='JSON Params', compute='_compute_json_params', default='{}', store=True, readonly=True)
    response = fields.Text(string='Response', readonly=True)
    payload = fields.Text(string='Payload')
    rendered_XML_payload = fields.Text(
        string='Rendered XML Payload', compute="_compute_rendered_payload", readonly=True, store=True)
    rendered_JSON_payload = fields.Text(
        string='Rendered JSON Payload', compute="_compute_rendered_payload", readonly=True, store=True)

    log_ids = fields.One2many('log.lines', 'server_id', readonly=True)
    chatter = fields.Boolean(string='Send log to chat')

    @api.depends('payload')
    def _compute_rendered_payload(self):
        for server in self:
            if server.payload and server.resource_ref:
                server.rendered_XML_payload = server._render_template_qweb(
                    server.resource_ref)
                server.rendered_JSON_payload = server.xml2json(
                    ET.XML(server._render_template_qweb(server.resource_ref)))
            else:
                server.rendered_JSON_payload= "{}"
                server.rendered_XML_payload= "<>"
                

    def _run_action_api_call(self, eval_context=None):
        self.ensure_one()
        params = json.loads(self.json_params) or None
        rendered_JSON_payload = self.xml2json(
            ET.XML(self._render_template_qweb()))
        local_payload = None if not self.payload else json.dumps(
            rendered_JSON_payload)

        url = self.api_id.url
        method = self.api_id.method
        headers = json.loads(self.translate_o2m(
            self.api_id.header_ids)) or None

        api_response = None

        try:
            if method == 'get':
                api_response = requests.get(
                    url, headers=headers, params=params)
            if method == 'post':
                api_response = requests.post(
                    url, headers=headers, data=local_payload)
        except Exception:
            if self.chatter:
                self._send_message(api_response.status_code)
            raise UserError(
                "Error: something went wrong please retry or check the logs")

        self.env['log.lines'].create({
            'call': "%s %s" % (method, url),
            'response': api_response.text,
            'server_id': self.id,
            'status':  api_response.status_code,
        })
        
        if self.chatter:
            self._send_message(api_response.status_code)

        if api_response.status_code >= 400:
            raise UserError("Error: -> %s" % api_response.text)

        
    @api.depends('params_ids')
    def _compute_json_params(self):
        for server in self:
            server.json_params = server.translate_o2m(server.params_ids)

    def translate_o2m(self, one2many_field):
        json_field = {line.key: line.value for line in one2many_field}
        return json.dumps(json_field)

    def _render_template_qweb(self, record=None):
        try:

            model = self.model_id.model
            values = {
                'object': record or self.env[model].search([('id', "=", self._context.get('active_id', False))]),
            }
            render_result = self.env['ir.qweb']._render(
                html.fragment_fromstring(self.payload), values)
        except Exception:
            return None
        return str(render_result).replace("<br>", "")

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

    def _send_message(self, message=400):
        try:
            odoo_bot = self.env.ref('base.partner_root')
            model = self.model_id.model
            if message < 200:
                message_name = "Info"
            elif message >= 200 and message < 400:
                message_name = "Ok"
            else:
                message_name = "Error"

            self.env[model].search([('id', "=", self._context.get('active_id', False))]).with_user(odoo_bot).message_post(subject="API call made :)", body=(
                "%s: status:%s <a href=# data-oe-model=ir.actions.server data-oe-id=%s>%s</a>") % (message_name, message, self.id, self.name))
        except Exception:
            pass


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
    status = fields.Integer(string='Status')
