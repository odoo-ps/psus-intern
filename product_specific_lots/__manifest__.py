# -*- coding: utf-8 -*-
{
    'name': 'Product specific lots',
    'sumary': 'Access rights changes',
    'description': """
        Give access rights over specific fields to sales persons and sales admin
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['product', 'mrp'],
    'data': [
        'views/product_inherit_lot_number.xml',
        'views/mrp_productionn_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
