# -*- coding: utf-8 -*-

{
    'name': 'NYPW Shoes',
    'application': True,
    'summary': """App to manage NY P&W Shoes""",
    'description': """
        App to manage NY P&W Shoes:
    """,
    'license': 'LGPL-3',
    'author': 'Odoo',
    'website': 'www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base', 'product'],
    'data': [
        'views/product_views_inherit.xml',
    ],
    'demo': [
    ]
}
