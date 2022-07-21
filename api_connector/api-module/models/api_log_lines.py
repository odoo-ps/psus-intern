from odoo import fields, models


class LogLines(models.Model):
    _name = 'log.lines'
    _description = 'API logs lines'

    log_id = fields.Many2one('api.logs', string='API Logs', readonly=True)
    server_id = fields.Many2one('ir.actions.server', string='API')
    call = fields.Char(string='Call', readonly=True)
    method = fields.Char(string='Method', readonly=True)
    response = fields.Text(string='Response', readonly=True)
    status = fields.Integer(readonly=True)
