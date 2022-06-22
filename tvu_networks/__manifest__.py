# -*- coding: utf-8 -*-
{
    'name': "TVU networks",
    'summary': """automatically cancel quotations which are no longer relevant, as defined by the quotation passing 
    its expiration date.""",
    'description': """
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'data/ir_cron_data.xml'
    ],
    'demo': [
    ]
}
