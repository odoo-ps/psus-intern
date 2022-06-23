# -*- coding: utf-8 -*-

{
    'name': 'Access Rights Changes',
    'summary': 'A module to change access rights',
    'description': """
    A module to change access rights
    Author: yall
    task: 2874549
    """,
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '14.0.0.1',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/res_partner_create_form_inherit.xml'
    ],
    'license': 'OPL-1',
}