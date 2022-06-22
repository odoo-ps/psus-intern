# -*- coding: utf-8 -*-
{
    'name': 'Odoo Schedule',
    'sumary': 'Mindesa : Scheduled Action to Confirm RFQs',
    'description': """
        odoo schedule helps to schedule the action to confirm RFQs
    """,
    'author': 'EduardoCedillo(eacm)',
    'category': 'Purchase',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'data/cron.xml',
    ],
}
