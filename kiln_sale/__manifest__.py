# -*- coding: utf-8 -*-
{
    'name': "Kiln & Dryer Job Number Automation",

    'summary': 'Automatically assign job number and plant code.',

    'description': """
        Automatically assign job number and plant code.

        On Sale Order (SO), assign job number based on a chosen prefix.
        On Customers, when their first SO is confirmed they will be assigned a plant code
        based on their company's name.

        Task ID: 2874285
    """,

    'author': "Odoo Inc",
    'website': "https://www.odoo.com/",
    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'auto_install': False,

    'category': 'Custom Development',
    'version': '1.0',

    'depends': ['sale'],

    'data': [
        'views/views.xml',
    ],
}
