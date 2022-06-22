# -*- coding: utf-8 -*-
{
    'name': "Auto-cancel Expired Quotations",

    'license': 'OPL-1',

    'summary': 'Cancel quotations that are due to expire every midnight.',

    'description': """
        Cancel quotations that are due to expire every midnight.

        This module adds a scheduled action set to run at midnight,
        which will auto-cancel any quotations that have just expired.

        Task source: 2874269
    """,

    'author': "Odoo Inc",
    'website': "https://odoo.com",

    'category': 'Custom Development',
    'version': '1.0',

    'application': False,
    'installable': True,
    'auto_install': True,

    'depends': ['sale'],

    'data': [
        'data/cron.xml',
    ],
}
