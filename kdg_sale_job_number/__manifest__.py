# -*- coding: utf-8 -*-
{
    'name': "KDG - Job number, Plant code",

    'description': """
        Adds custom Job Number field on Sales Orders and Plant Number field on Customer
        Task ID: 2874101
        """,

    'author': 'Odoo Inc',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    'depends': ['sale_management'],

    'data': [
       'views/sale_order_views.xml',
       'views/res_partner_views.xml',
       'data/job_number_sequence.xml'
    ],

    'application': False,
    'installable': True,
    'auto_install': True,
}
