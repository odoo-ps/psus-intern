# -*- coding: utf-8 -*-
{
    'name': 'Access Rights Change',
    'version': '1.0',
    'description': """
        Users of the group sales/own documents only and sales/all documents
        can enter the value of sales person and pricelist when they create a contact.
    """,
    'summary': 'Users of the group sales/own documents only and sales/all documents can enter the value of sales person and pricelist when they create a contact.',
    'author': 'Odoo Inc',
    'website': 'Custom Development',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': ['product'],
    'data': [
        'views/res_partner.xml'
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
