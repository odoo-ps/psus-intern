# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes',

    'summary': """Make `Sales Price` a calculated field based on `Pair per Case` and `Price per Pair` fields""",

    'description': """
        task_id: 2874431
        Add Three fields:
        - Pair per Case
        - Price per Pair
        - Sales Price = Pair per Case * Price per Pair
        To product.template model
    """,

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'Custom development',

    'version': '15.0.1.0',

    'depends': ['product'],

    'data': [
        'views/product_views_inherit.xml',
    ],

    'demo': [

    ],

    'auto_install': False,

    'installable': True,

    'application': False,
}
