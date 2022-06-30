# -*- encoding: utf-8 -*-

{
    'name': 'Timesheet Validation Pipeline',
    'version': '1.0',
    'license': 'OPL-1',
    'author': 'Odoo Inc',
    'category': 'Training',
    'summary': 'Implmented timesheet pipeline based on permissions',
    'description': """
        There are several levels of approval for timesheets. A project manager must approve it, and then a supervisor, and then finally 
        and administrator. If the timesheet is invalidated at any point, it will be reset to a draft and the creator of the timesheet
        will be notified.
    """,
    'depends': ['account', 'hr_timesheet', 'mail'],
    'data': [
        'security/access-levels-security.xml',
        'security/ir.model.access.csv',
        'views/account_analytic_line_views.xml'
    ],
}



