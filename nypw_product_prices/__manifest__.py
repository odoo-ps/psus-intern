# -*- coding: utf-8 -*-

{
    'name': "Auto Calculate Price",

    'summary': """NY P&W Shoes Auto Calculate Price""",

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'product',
    ],

    # always loaded
    'data': [
        'views/product_template_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
