# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes',

    'summary': """Add new fields to product.template model""",

    'description': """
        Add Three fields:
        - Pair per Case
        - Price per Pair
        - Sales Price
        To product.template model
    """,

    'author': 'yazh',

    'website': 'https://www.odoo.com',

    'category': 'Sales',

    'version': '0.1',

    'depends': ['product'],

    'data': [
        'views/product_views_inherit.xml',
    ],

    'demo': [

    ],
}
