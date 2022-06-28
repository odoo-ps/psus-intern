# -*- coding: utf-8 -*-

{
    'name': 'Product Specific Lots',
    'summary': """Module to create specific lot numbers related to the product.""",
    'description': """
        This module lets the user create a prefix based on nomenclature related to the product.
        Once this prefix is created, in the manufacturing process we should be able to add the lot number
            with the prefix created in the product.template form.
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '14.0.1.0.0',
    'depends': ['product', 'mrp'],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
