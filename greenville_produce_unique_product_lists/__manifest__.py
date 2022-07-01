# -*- coding: utf-8 -*-

{
    'name': "Greenville Produce - Unique product lists per customer",
    'summary': """
    """,
    'description': """
        task_id: 2874333
        
        Added a product list to 'res.partner' model to provide unique product lists per customer
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['website_sale'],
    'data': [
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        'views/product_lists_menuitem.xml',
        'views/product_lists_views.xml',
        'views/contact_views_inherit.xml',
    ]
}
