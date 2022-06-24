# -*- coding: utf-8 -*-

{
    'name': 'Product Configuration With Variants.',
    'summary': """Module to create product configuration with variants.""",
    'description': """
        We need to create product variants with configuration. We also need to generate a unique code for every variant based on the attribute values.
        This code only needs to be created once that configuration is ordered, we don't need all possible configuration codes.
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '15.0.1.0.0',
    'depends': ['product'],
    'data': [
        'views/product_attribute_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
