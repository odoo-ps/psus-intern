from odoo import api, fields, models

class SurveyQuestionArgument(models.Model):
    _name = 'survey.question_argument'

    _description = 'Describes the expected function arguments when writing up a coding question in Odoo\'s survey module.'

    question_id = fields.Many2one('survey.question')

    name = fields.Char('Name', required=True)

    type = fields.Selection([
        ('int', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('array', 'Array'),
        ('dictionary', 'Dictionary'),
    ], string='Type', default='int', store=True)
