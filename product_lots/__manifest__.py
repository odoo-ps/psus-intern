# -*- coding: utf-8 -*-
{
    'name': 'Greenville Produce',
    'sumary': ' Product Lists Module ',
    'description': """
        Module to add product lists for eCommerce website
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
        'mrp'
    ],
    'data': [
        'views/product_template_views_inherit.xml',
        'views/mrp_production_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
