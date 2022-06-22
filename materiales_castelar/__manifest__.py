# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Materiales Castelar',

    'summary': """Make sure difference warehouses will not receive more than the demanded quantity""",

    'description': """
        Task ID: 2874415
        Warehouse should not receive more than ordered quantity. 
        If it does, warning should appear 
        and the user must enter the correct quantity (<= demand)
    """,

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'Custom Development',

    'version': '15.0.1.0',

    'depends': ['stock'],

    'data': [

    ],

    'demo': [

    ],

    'auto_install': False,

    'installable': True,

    'application': False,

    'license': 'LGPL-3',
}
