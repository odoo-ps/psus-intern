# -*- coding: utf-8 -*-
{
    'name': 'Auto-confirm RFQs',
    'version': '1.0',
    'description': 'Auto-confirm RFQs from branch stores to the Central Store',
    'summary': '',
    'author': 'Odoo Inc',
    'website': 'https://odoo.com',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': [
        'purchase'
    ],
    'data': [
        'data/cron.xml'
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
