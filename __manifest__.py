# -*- coding: utf-8 -*-

{
    'name': 'Greenville Produce Unique Products Lists',

    'summary': """
        Displays product lists that are unique with respect to their customers""",

    'description': """
        Dispaly product lists that only display list-specific products.
        If no list is selected, all products are displayed. Task ID: 2873901
    """,

    'author': 'Odoo',

    'website': 'https://www.odoo.com',

    'category': 'Sales',

    'version': '14.0',
    
    'depends': ['website_sale'],
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_partner.xml',
    ],

    'license': 'OEEL-1',
}