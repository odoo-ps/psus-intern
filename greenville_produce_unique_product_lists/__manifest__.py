# -*- coding: utf-8 -*-

{
    'name': "Greenville Produce: Unique product lists per customer",
    'summary': """
    """,
    'description': """
        task_id: 2874333
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'views/product_lists_menuitem.xml',
        'views/product_lists_views.xml',
        'views/contact_views_inherit.xml',
    ]
}
