# -*- coding: utf-8 -*-
{
    'name': 'P&W shoes',
    'sumary': 'Add autocalculated price to shoes',
    'description': """
        App to add Pair per Case and price per pair to product
        and autocalculated the product price,
    """,
    'author': 'Odoo PS',
    'category': 'Invoice',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'product',
    ],
    'license': 'OPL-1',
    'data': [
        'views/product_template_views_inherith.xml'
    ],
}
