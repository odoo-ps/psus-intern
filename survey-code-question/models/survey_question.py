# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection(selection_add=[('python_question', 'Python Question')])

    def validate_question(self, answer, comment=None):
        res = super().validate_question(self, answer, comment)
        if not res:
            #leave in list for other kind of code questions
            if answer or self.question_type in ['python_code']:
                return self._validate_python_question(answer)
        return {}

    def _validate_python_question(self, answer):
        try:
            res = eval(answer)
        except:
            #TODO better runtime error handling
            print('Error while evaluating code')

        assert res == 2, 'wrong.'
        return {}
