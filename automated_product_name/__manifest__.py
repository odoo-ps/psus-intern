# -*- coding: utf-8 -*-
{
    'name': 'Automated Product Names',
    'sumary': ' Generate product names automatically ',
    'description': """
        On creation, generate product name automatically, based on product category. 
        Also, genereate an UPC based on the gender and category of the product.
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'data': [
        'views/product_category_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
