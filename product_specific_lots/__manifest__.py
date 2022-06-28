# -*- coding: utf-8 -*-

{
    'name': 'Product Specific Lots',
    'summary': 'Create a unique prefix per product for lot serialization',
    'description': 'Create a unique prefix per product for lot serialization',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'manufacturing',
    'version': '0.1',
    'depends': ['mrp'],
    'data': [
        'views/product_template_views_inherit.xml'
    ]
}