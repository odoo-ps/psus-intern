# -*- coding: utf-8 -*-

{
    'name': 'Auto Calculate Price',
    'summary': 'A module to auto calculate the price for pairs of shoes in the order',
    'description': """
    A module to auto calculate the price for pairs of shoes in the order
    using computed and inverse fields.
    Author: yall
    Task: 2874547
    """,
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '15.0.0.1',
    'depends': [
        'sale',
    ],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
