# -*- coding: utf-8 -*-
{
    'name': "Product Configuration with Variants",

    'summary': 'A module to use the product configurator to calculate price on a set of inputs',
    'description': """
    A module to calculate part numbers and price.
    Task: 2873990
    """,
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '14.0.0.1',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_template_attributes_values_inherit.xml',
    ],
    'license': 'OPL-1',
}
