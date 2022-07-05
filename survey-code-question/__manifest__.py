# -*- coding: utf-8 -*-

{
    'name': 'Code Surveys',
    'version': '15.0.0.1',
    'category': 'Survey',
    'summary': 'Create code surveys and validate answers',
    'Author': 'Odoo PS',
    'description': """
Create Code questions and assert results
========================================

It depends on the answers or reviews of some questions by different users. A
survey may have multiple pages. Each page may contain multiple questions and
each question may have multiple answers. Different users may give different
answers of question and according to that survey is done. Partners are also
sent mails with personal token for the invitation of the survey.
Authors: yall, daav
task: 2856501
    """,
    'depends': [
        'survey',
    ],
    'data': [
        'views/survey_user_input_line_view_form_inherit.xml',
        'views/survey_question_form_inherit.xml',
        'views/survey_templates.xml',
    ],
    'demo': [
    ],
    'license': 'OPL-1',
}
