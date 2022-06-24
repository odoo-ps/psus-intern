# -*- coding: utf-8 -*-

{
    'name': 'Change Access Rights of fields based on groups.',
    'summary': """Module to change the access rights of some fields based on groups.""",
    'description': """
        This modules allows users from the groups 'sales/all documents' and 'sales/own documents only' 
        to create a new contact and assign themselves as the salesperson for the contact and their pricelist; 
        however when editing the contact, those fields should be readonly. 
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/res_partner_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
