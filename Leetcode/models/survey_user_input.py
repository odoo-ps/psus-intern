from odoo import api, fields, models, _


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'


    def save_lines(self, question, answer, comment=None):
        old_answers = self.env['survey.user_input.line'].search([
            ('user_input_id', '=', self.id),
            ('question_id', '=', question.id)
        ])

        if question.question_type in ['char_box', 'text_box', 'numerical_box', 'date', 'datetime', 'code_box']:
            self._save_line_simple_answer(question, old_answers, answer)
            if question.save_as_email and answer:
                self.write({'email': answer})
            if question.save_as_nickname and answer:
                self.write({'nickname': answer})

        elif question.question_type in ['simple_choice', 'multiple_choice']:
            self._save_line_choice(question, old_answers, answer, comment)
        elif question.question_type == 'matrix':
            self._save_line_matrix(question, old_answers, answer, comment)
        else:
            raise AttributeError(question.question_type + ": This type of question has no saving function")


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'
   
    answer_type = fields.Selection(selection_add=[('code_box',_('Code Text box'))])
    value_code_box = fields.Char('Code answer')
