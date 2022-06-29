# -*- coding: utf-8 -*-

{
    'name': 'Product Automation',
    'summary': 'Automates the process of creating a product name',
    'description': 'Automates the process of creating a product name',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'license': 'OPL-1',
    'version': '0.1',
    'depends': ['sale_management'],
    'data': [
        'views/product_category_views_inherit.xml',
        'views/product_product_views_inherit.xml',
        'security/nypw_security.xml',
        'security/ir.model.access.csv'
    ]
} 