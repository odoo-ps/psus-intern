# -*- coding: utf-8 -*-

{
    'name': 'Library Management Module',
    'summary': 'Module meant for managing library data, such as books and customers. Made for Odoo onboarding traning purposes.',
    'author': 'Justin Deng (jden)',
    'category': 'Training',
    'depends': ['base'],
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/book_views.xml'
    ],
    'demo':['demo/library_demo.xml']
}

