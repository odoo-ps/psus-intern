# -*- coding: utf-8 -*-

{
    'name': 'TV quotation',

    'application': False,

    'summary': """App to cancel quotations at midnight""",

    'description': """Task ID: 2874296
        Expected to cancel all expired quotations at midnight every day.
    """,

    'author': 'Odoo Inc',

    'category': 'Inventory',

    'version': '1.0',

    'depends': ['sale'],

    'license': 'OPL-1',

    'data' : [
        'data/cron.xml',
    ],
}