import traceback
from odoo import api, fields, models, _
from ..tools import safe_compile


class SurveyQuestion(models.Model):
	_inherit = 'survey.question'

	question_type = fields.Selection(selection_add=[('code_box',_('Code Text box'))])
	answer_code_box = fields.Char(_('Coding correct answer'), help=_('Correct code output for this question.'))
	argument_ids = fields.One2many('survey.question_argument', 'question_id')
	function_name = fields.Char('Function Name', help='The name of the function the candidate should write', default='solution', required=True)
	function_template = fields.Char('Function Template',compute='_compute_function_template', store=True)
	test_ids = fields.One2many('survey.question_test', 'question_id')
	code_exec_time_limit = fields.Integer('Execution Time limit (s)', default=4)
	validation_error_msg = fields.Char('Validation Error message', compute='_compute_validation_error_msg',translate=True, default=lambda self: _("The answer you entered is not valid."))
	validation_required = fields.Boolean('Validate Entry', compute='_compute_validation_required')
	value_test_code = fields.Char('Code test')

	@api.depends('question_type')
	def _compute_validation_required(self):
		for question in self:
			if question.question_type == 'code_box':
				question.validation_required = True
			else:
				question.validation_required = False

	@api.depends('validation_required', 'question_type', 'argument_ids', 'function_name')
	def _compute_validation_error_msg(self):
		for question in self:
			if question.question_type == 'code_box':
				question.validation_error_msg = _("The function must be named '%s' and must have %s arguments.", question.function_name, len(question.argument_ids))
			else:
				question.validation_error_msg = _("The answer you entered is not valid.")

	@api.depends('question_type', 'scoring_type', 'answer_date', 'answer_datetime', 'answer_numerical_box', 'answer_code_box')
	def _compute_is_scored_question(self):
		super()._compute_is_scored_question()
		for question in self.filtered(lambda q: (q.question_type == 'code_box')):
			if not question.is_scored_question:
				if question.answer_code_box:
					question.is_scored_question = True
				else:
					question.is_scored_question = False

	@api.depends('argument_ids', 'function_name')
	def _compute_function_template(self):
		for question in self.filtered(lambda q: (q.question_type == 'code_box')):
			question.function_template = f'class Solution:\n\tdef {question.function_name}(self, '
			comma, arg_counter = ', ', 0
			for arg in question.argument_ids:
				comma = '' if arg_counter + 1 == len(question.argument_ids) else ', '
				question.function_template += arg.name + comma
				arg_counter += 1

			question.function_template += '):\n\t\treturn None'

	def validate_question(self, answer, comment=None):
		res = super().validate_question(answer)
		if not res:
			if answer and self.question_type == 'code_box':
				return self._validate_code_box(answer)
			elif not answer and self.question_type == 'code_box' or not answer and self.question_type != 'code_box':
				return {self.id: self.validation_error_msg}
			return {}
		else:
			return res
		
	def _validate_code_box(self, answer):
		"""
		This code validates the user-provided code in the survey module
		It only assures that the class is named correctly, methods are declared
		"""
		try:
			code_obj_config = safe_compile.safe_compile(answer)
		except (SyntaxError, IndentationError):
			return {self.id: traceback.format_exc()}
		code_obj = code_obj_config['code_obj']
		if 'Solution' not in code_obj.co_consts:
			return {self.id: self.validation_error_msg}
		solution_class_name_index = code_obj.co_consts.index('Solution') - 1
		solution_class_co_names = code_obj.co_consts[solution_class_name_index].co_names
		if self.function_name not in solution_class_co_names:
			return {self.id: self.validation_error_msg}
		class_obj_name = code_obj.co_names[-1] + '.' + self.function_name
		main_method_ind = code_obj.co_consts[solution_class_name_index].co_consts.index(class_obj_name) - 1
		if code_obj.co_consts[solution_class_name_index].co_consts[main_method_ind].co_argcount != (len(self.argument_ids) + 1):
			return {self.id: self.validation_error_msg}
		return {}
