from odoo import fields, models


class IrActionsServerParamsLines(models.Model):
    _name = 'ir.actions.server.params.lines'
    _description = "Actions Server Params O2M Lines"

    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    server_id = fields.Many2one('ir.actions.server', string='API')
