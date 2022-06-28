# -*- coding: utf-8 -*-
{
    'name': 'Odoo Lot',
    'sumary': 'Product Specific Lots',
    'description': """
        odoo lot helps you to create a unique product lot number per product created
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale', 'mrp'],
    'license': 'OPL-1',
    'data': [
        'views/product_template_views_inherit.xml',
        'views/mrp_production_views_inherit.xml',
    ],
}
