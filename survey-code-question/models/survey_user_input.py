# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'


    def save_lines(self, question, answer, comment=None):
        super().save_lines(question, answer, comment)

        old_answers = self.env['survey.user_input.line'].search([
            ('user_input_id', '=', self.id),
            ('question_id', '=', question.id)
        ])

        if question.question_type in ['code_box']:
            logging.info(msg='Is code box yessir')
            self._save_line_simple_answer(question, old_answers, answer)
        
        super().save_lines(question, answer, comment)

    def _get_line_answer_values(self, question, answer, answer_type):
        vals = super()._get_line_answer_values(question, answer, answer_type)
        logging.info(msg=f'Vals: {vals}')
        return vals

class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'

    answer_type = fields.Selection(selection_add=[('code_box', _('Code Text box'))])
    value_code_box = fields.Char('Code answer')
