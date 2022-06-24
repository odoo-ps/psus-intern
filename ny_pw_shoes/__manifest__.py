# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes',

    'application': False,

    'summary': """App to calculate price of shoes""",

    'desciption' : """Task ID: 2874296
        Expected to calculate price of shoes based on price per pair and pair per case.
    """,

    'author': 'Odoo Inc',

    'category': 'Inventory',

    'version': '1.0',

    'depends': ['sale'],

    'license': 'OPL-1',

    'data': [
        'views/product_views.xml',
    ],
}