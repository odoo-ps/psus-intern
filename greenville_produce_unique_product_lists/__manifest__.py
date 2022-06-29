# -*- coding: utf-8 -*-

{
    'name': "Greenville Produce - Unique product lists per customer",
    'summary': """
    """,
    'description': """
        task_id: 2874333
        
        Added a new tab with a new field 'Product List' to 'res.partner'
        Created a new model for products list
        Added a new menuitem for 'Product List' under Sales -> Products
        Inherited '_get_search_domain' method of WebsiteSale controller to filter according to Product List assigned to the user
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        'views/product_lists_menuitem.xml',
        'views/product_lists_views.xml',
        'views/contact_views_inherit.xml',
    ]
}
