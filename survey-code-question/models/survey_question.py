# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection(selection_add=[('code', 'Coding question')])

    def validate_question(self, answer, comment=None):
        res = super().validate_question(answer, comment)
        if not res:
            if self.question_type == 'code':
                return self._validate_code_box(answer)
            else:
                return {}

    def _validate_code_box(self, answer):
        #FIXME answer is an empty list -> it may be due to lack of save_lines handling of 'code' case OR _get_line_values.
        try:
            code_output = eval(answer)
        except:
            return {self.id: _('Error evaluating code. Please check for errors.')}
        assert code_output == 2, 'Wrong Answer'
        return {}
