from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models
import json


# class ApiResponse(models.Model):
#     _name = 'api.response'
#     _description = 'API Response'
    
#     #response_lines = fields.One2many('api.response.lines', 'api_response_id', string='Response Lines')
#     api_id = fields.Many2one('api.connection', string='API')
    

# class ApiResponseLines(models.Model):
#     _name = 'api.response.lines'
#     _description = "API  response Lines"
    
#     #api_response_id = fields.Many2one('api.response', string='API Response')
#     key = fields.Char(string='Key')
#     model_value = fields.Char(string='Model Value')
    
        
        
        
        
    

