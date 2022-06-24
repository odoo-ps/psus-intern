# -*- coding: utf-8 -*-

{
    'name': 'NYPW Shoes Product Prices',
    'application': True,
    'summary': """Calculate 'Sales Price' based on 'Pair per case' and 'Price per pair' fields""",
    'description': """
        task_id: 2874358
        Added 3 new fields to product.template model:
        - Pair per Case
        - Price per Pair
        - Sales Price (Calculated) = Pair per Case * Price per Pair
        
    """,
    'license': 'OPL-1',
    'author': 'Odoo Inc',
    'website': 'www.odoo.com',
    'category': 'Training',
    'version': '1.0',
    'depends': ['product'],
    'data': [
        'views/product_views_inherit.xml',
    ],
    'demo': [
    ]
}
