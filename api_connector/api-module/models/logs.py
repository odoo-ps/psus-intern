from odoo import fields, models


class Logs(models.Model):
    _name = 'logs'
    _description = 'API logs'
    
    
    log_lines_ids = fields.One2many('log.lines', 'log_id', string='Logs')
    server_ids = fields.One2many('ir.actions.server', 'log_ids', string='Server Actions')


    
