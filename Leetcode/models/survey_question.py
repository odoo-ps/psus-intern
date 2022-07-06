from odoo import fields, models, _


class SurveyQuestion(models.Model):
  _inherit = 'survey.question'

  question_type = fields.Selection(selection_add=[('code_box',_('Code Text box'))])
  
  def validate_question(self, answer, comment=None):
    res = super().validate_question(answer)
    if not res:
      if answer and self.question_type == 'code_box':
        return self._validate_code_box(answer)
      return {}
      
    
  def _validate_code_box(self, answer):
    if self.validation_required:
            if not (self.validation_length_min <= len(answer) <= self.validation_length_max):
                return {self.id: self.validation_error_msg}
    return {}
