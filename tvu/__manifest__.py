# -*- coding: utf-8 -*-
{
    'name': "tvu",

    'summary': """
        For Client TVU""",
    'description': """
        This module provides Auto cancel expired quotations for TVU.
        Task ID : 2874159
    """,

    'author': "Odoo Inc",
    'website': "http://www.odoo.com",

    'category': 'Custom Development',
    'version': '1.0',

    'depends': ['base','sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/expired_cancel.xml'
    ],
    'demo': [
    ],
}
