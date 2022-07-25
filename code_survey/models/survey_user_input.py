import traceback
from types import FunctionType
from ..tools import safe_compile
import logging
from odoo import api, fields, models, _


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    value_test_code = fields.Char('Code test')
    arguments_ids = fields.Many2one('survey.question_argument', ondelete='cascade')

    def _signal_handler(self, signum, frame):
        raise Exception("Your proposed solution timed out.")

    def _fetch_tests(self, question, isTest=False):
        #comes from the controller:
        if isinstance(question, str):
            question = self.env['survey.question'].search([
                ('id', '=', question)
            ])
        test_dict = {}
        for test in question.test_ids:
            if isTest and test.is_hidden:
                continue
            #TODO check datatype (not always integers)
            arg_tuple = tuple([int(i) for i in test.input_.split(',')])
            test_dict[arg_tuple] = test.output
        return test_dict

    def _run_code(self, question, solution, args):
        try:
            error = ''
            func_name = question.function_name
            code_output = str(getattr(solution, func_name)(*args))
        except:
            code_output = ''
            error = traceback.format_exc()
        return code_output, error

    def build_solution_class(self, question, code_obj_config):
        code_obj = code_obj_config['code_obj']
        if 'Solution' not in code_obj.co_consts:
            raise ValueError('Class named "Solution" not provided.')

        for name in code_obj.co_names:
            try:
                code_obj_config['globals_dict'][f'{name}'] = safe_compile._import(name, code_obj_config['globals_dict'])
            except ImportError:
                continue

        main_method_name = question.function_name
        #wrap everything in a class (Solution)
        solution_class_name_index = code_obj.co_consts.index('Solution') - 1
        solution_class_co_names = code_obj.co_consts[solution_class_name_index].co_names
        if main_method_name not in solution_class_co_names:
            raise ValueError(f'{main_method_name} not provided')
        methods = {}
        
        for name in solution_class_co_names:
            class_obj_name = code_obj.co_names[-1] + '.' + name
            if class_obj_name in code_obj.co_consts[solution_class_name_index].co_consts:
                name_ind = code_obj.co_consts[solution_class_name_index].co_consts.index(class_obj_name) - 1
                methods[name] = FunctionType(code_obj.co_consts[solution_class_name_index].co_consts[name_ind], code_obj_config['globals_dict'], name)

        Solution = type("Solution",
                    (),
                    methods)
            
        return Solution()
        
    def test_code(self, question, answer):
        test_dict = self._fetch_tests(question, isTest=True)
        code_obj_config = safe_compile.safe_compile(answer)
        solution = self.build_solution_class(question, code_obj_config)
        test_no = 1
        self.value_test_code = ''

        for test_args, test_output in test_dict.items():
            code_output, error = self._run_code(question, solution, test_args)
            if not error:
                self.value_test_code += f'Test #{test_no}: Input = {test_args} -> Output = {code_output} Expected = {test_output}\n'
            else:
                self.value_test_code += f'Test #{test_no}: Input = {test_args} -> Output = {error} Expected = {test_output}\n'
            test_no += 1
        self.env['survey.question'].sudo().search([('id', '=', question.id)], limit=1).value_test_code = self.value_test_code
        return {}

    def save_lines(self, question, answer, comment=None):
        old_answers = self.env['survey.user_input.line'].search([
            ('user_input_id', '=', self.id),
            ('question_id', '=', question.id)
        ])

        if question.question_type in ['char_box', 'text_box', 'numerical_box', 'date', 'datetime', 'code_box']:
            if question.question_type == 'code_box':
                #careful, this is a dictionary
                code_obj_config = safe_compile.safe_compile(answer)
                test_dict = self._fetch_tests(question)
                solution = self.build_solution_class(question, code_obj_config)
                correct = 0
                test_no = 1
                self.value_test_code = ''
                for test_args, test_output in test_dict.items():
                    code_output, error = self._run_code(question, solution, test_args)
                    if not error and code_output == test_output:
                        correct += 1
                        self.value_test_code += f'Test #{test_no}: Input = {test_args} -> Output = {code_output} Expected = {test_output}\n'
                        test_no += 1
                    elif error:
                        self.value_test_code += f'Test #{test_no}: Input = {test_args} -> Output = {error} Expected = {test_output}\n'
                self.env['survey.question'].sudo().search([('id', '=', question.id)], limit=1).value_test_code = self.value_test_code
                question_score = correct/len(test_dict)
                self._save_line_code_answer(question, question_score, answer)
            else:
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

    def _get_line_answer_values(self, question, answer, answer_type, question_score=0):
        vals = super()._get_line_answer_values(question, answer, answer_type)
        if answer_type == 'code_box' and question.is_scored_question:
            vals['correct_tests'] = question_score
        return vals
    
    def _save_line_code_answer(self, question, correct_score, answer):
        answer = '# Overall score for this question: ' + str(correct_score * 100) + '%' + '\n' + answer
        vals = self._get_line_answer_values(question, answer, question.question_type, correct_score)
        return self.env['survey.user_input.line'].create(vals)


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'
   
    answer_type = fields.Selection(selection_add=[('code_box',_('Code Text box'))])
    value_code_box = fields.Char('Code answer')
    correct_tests = fields.Float('Number of Correct Tests', default=0.0)

    @api.model
    def _get_answer_score_values(self, vals, compute_speed_score=True):
        res = super()._get_answer_score_values(vals, compute_speed_score)
        answer_type = vals.get('answer_type')
        if answer_type != 'code_box':
            return res

        user_input_id = vals.get('user_input_id')
        question_id = vals.get('question_id')
        if not question_id:
            raise ValueError(_('Computing score requires a question in arguments.'))
        question = self.env['survey.question'].browse(int(question_id))

        answer_is_correct = False
        answer_score = 0

        if question.is_scored_question:
            answer = vals.get('correct_tests')

            if answer:
                answer_score = question.answer_score * float(answer)
                answer_is_correct = True if answer_score > 0 else False
        
        if compute_speed_score and answer_score > 0:
            user_input = self.env['survey.user_input'].browse(user_input_id)
            session_speed_rating = user_input.exists() and user_input.is_session_answer and user_input.survey_id.session_speed_rating
            if session_speed_rating:
                max_score_delay = 2
                time_limit = question.time_limit
                now = fields.Datetime.now()
                seconds_to_answer = (now - user_input.survey_id.session_question_start_time).total_seconds()
                question_remaining_time = time_limit - seconds_to_answer
                # if answered within the max_score_delay => leave score as is
                if question_remaining_time < 0:  # if no time left
                    answer_score /= 2
                elif seconds_to_answer > max_score_delay:
                    time_limit -= max_score_delay  # we remove the max_score_delay to have all possible values
                    score_proportion = (time_limit - seconds_to_answer) / time_limit
                    answer_score = (answer_score / 2) * (1 + score_proportion)
        
        return {
            'answer_is_correct': answer_is_correct,
            'answer_score': answer_score
        }
