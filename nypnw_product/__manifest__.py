# -*- coding: utf-8 -*-
{
    'name': "Product Name & UPC Generator",

    'summary': 'Auto-generate product name and UPCs.',

    'description': """
        Auto-generate product name and UPCs.

        When a product category is assigned to a product, the product name is
        derived from the product category's assigned sequence.
        Alongside, a UPC based on product gender is auto-generated.

        Task ID: 2874271
    """,

    'author': "Odoo Inc",
    'website': "https://odoo.com",
    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'auto_install': False,

    'category': 'Custom Development',
    'version': '1.0',

    'depends': ['product'],

    'data': [
        'views/views.xml',
    ],
}
