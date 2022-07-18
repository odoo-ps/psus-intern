from odoo import fields, models


class LogLines(models.Model):
    _name = 'log.lines'
    _description = 'API logs'

    log_id = fields.Many2one('api.logs', string='API Logs')
    server_id = fields.Many2one('ir.actions.server', string='API')
    call = fields.Char(string='Call')
    response = fields.Text(string='Response')
    status = fields.Integer(string='Status')
