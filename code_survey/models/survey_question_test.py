from odoo import fields, models


class SurveyQuestionTest(models.Model):
    _name = 'survey.question_test'
    _description = 'Tests definition for coding challenges in survey module.'

    question_id = fields.Many2one('survey.question')
    input_ = fields.Char('Input')
    output = fields.Char('Expected Output')
    is_hidden = fields.Boolean('Hidden Test',default=False)
