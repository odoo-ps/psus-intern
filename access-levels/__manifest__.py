# -*- encoding: utf-8 -*-

{
    'name': 'access-levels',
    'version': '1.0',
    'license': 'OPL-1',
    'author': 'Odoo Inc',
    'summary': 'Implmented timesheet popeline based on permissions',
    'description': """
    """,
    'depends': ['account', 'analytic', 'analytic_enterprise', 'hr_timesheet', 'mail'],
    'data': [
        'security/access-levels-security.xml',
        'security/ir.model.access.csv',
        'views/modified-timesheet-actions.xml'
    ],
}



