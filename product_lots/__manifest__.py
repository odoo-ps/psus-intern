# -*- coding: utf-8 -*-
{
    'name': 'Product Specific Lots',
    'sumary': 'Add a specific lot for each product created',
    'description': """
        App a solt for each product created, with a list of abreviations for each product.
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'license': 'OPL-1',
    'data': [
        "views/product_view_inherit.xml",
        "views/mrp_production_view.xml",
    ],
}
