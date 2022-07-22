{
  'name':'Code Survey Question Module',
  'summary':'A module that implements a coding question in Odoo\'s survey app.', 
  'description':'''
Code Survey Question Module
===========================
This module contains the necessary elements that affect the Survey app in Odoo,
in order to get the option to create a question for a coding problem.
The creator of the survey can specify the expected output, and assign a score to that question.
Authors: daav, yall
Task: 2856501
  ''',
  'author':'Odoo PS',
  'category':'surveys',
  'version':'15.0.0.1',
  'depends':['survey'],
  'data':[
    'security/ir.model.access.csv',
    'views/survey_question_views_inherit.xml',
    'views/survey_templates_inherit.xml',
    'views/survey_templates_print_inherit.xml',
    'views/survey_user_views_inherit.xml',
  ],
  'assets':{
    'survey.survey_assets': [
        'code_survey/static/src/js/survey_form.js',
        'code_survey/static/src/scss/survey_templates_form.scss',
  ],
  },
  'license': 'OPL-1',
}
