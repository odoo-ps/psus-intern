# -*- coding: utf-8 -*-

{
    'name': 'Scheduled RFQs',
    'summary': 'A module to create automatically the RFQs',
    'description': 'A module to create automatically the RFQs  - yall',
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '14.0.0.1',
    'depends': [
        'purchase',
    ],
    'data': [
        'data/scheduled_rfqs_cron.xml',
    ],
    'license': 'OPL-1',
}
