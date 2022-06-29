# -*- coding: utf-8 -*-

{
    'name': 'Unique Product List - Greenville Produce',

    'summary': """Make unique product lists for each customer""",

    'description': """
        Task ID: 2874406
        Add "Product List" module under Sales/Products
        Add "eCommerce" Tab under Contacts form
        Enable filter functionality for Website - Shop
    """,

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'Custom Development',

    'version': '14.0.1.0',

    'depends': ['product', 'website'],

    'data': [
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        'views/product_list_views.xml',
        'views/product_list_menuitems.xml',
        'views/res_partner_views_inherit.xml',
    ],

    'demo': [

    ],

    'auto_install': False,

    'installable': True,

    'application': False,

    'license': 'OPL-1',
}
