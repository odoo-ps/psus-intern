# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'

    answer_type = fields.Selection(selection_add=[('code_box', _('Code Text box'))])

    value_code_box = fields.Char('Code answer')

    #TODO (i think) inherit save_lines and _get_line_answer values
