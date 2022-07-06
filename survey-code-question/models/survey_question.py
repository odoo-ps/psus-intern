# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection(selection_add=[('code_box', 'Coding question')])

    # TODO possible test suite
    answer_code_box = fields.Char('Correct coding answer', help='Correct output for this coding question.')

    @api.depends('question_type', 'scoring_type', 'answer_date', 'answer_datetime', 'answer_numerical_box', 'answer_code_box')
    def _compute_is_scored_question(self):
        super()._compute_is_scored_question()
        for question in self:
            if question.question_type == 'code_box' and question.answer_code_box:
                question.is_scored_question = True
            else:
                question.is_scored_question = False

    def validate_question(self, answer, comment=None):
        res = super().validate_question(answer, comment)
        if not res:
            if self.question_type == 'code_box':
                return self._validate_code_box(answer)
            else:
                return {}
        else:
            return res

    def _validate_code_box(self, answer):
        #FIXME answer is an empty list
        logging.info(msg=f'Answer received for validation: {answer}')
        try:
            code_output = eval(answer)
        except:
            return {self.id: _('Error evaluating code. Please check for errors.')}
        assert code_output == 2, 'Wrong Answer'
        return {}
