# -*- coding: utf-8 -*-
{
    'name': "Green Valley Sale Product List",

    'summary': """make a new product list for sale,""",

    'description': """
        []
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['sale','contacts','website_sale'],

    # always loaded
    'data': [
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        'views/product_list_menu_items.xml',
        'views/product_list_view.xml',
        'views/res_partner_inherit_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
