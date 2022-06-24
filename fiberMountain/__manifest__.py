# -*- coding: utf-8 -*-

{
    'name': 'Product Variants',
    'summary': 'A module to use the product configurator to calculate price on a set of inputs',
    'description': """
    A module to calculate part numbers and price.

    Author: yall
    Task: 2874541
    """,
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '14.0.0.1',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_template_attributes_values_inherit.xml'
    ],
    'license': 'OPL-1',
}
