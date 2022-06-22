# -*- coding: utf-8 -*-
{
    'name': 'Mindesa Schedule',
    'sumary': 'Mindesa : Scheduled Action to Confirm RFQs',
    'description': """
        moduel to schedule the action to confirm RFQs
    """,
    'author': 'Odoo PS',
    'category': 'Purchase',
    'version': '14.0.1.0.0',
    'depends': [
        'purchase',
    ],
    'license': 'OPL-1',
    'data': [
        'data/cron.xml'
    ]
}
