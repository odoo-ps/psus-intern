# -*- coding: utf-8 -*-
{
    'name': 'NYPW Shoes ',
    'sumary': 'Autocalculate Sales Price',
    'description': """
        Autocalculate prices. Auto calculate sales price according to pair per case and price per case fields in product_template model
    """,
    'author': 'Odoo PS',
    'category': 'Product',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'sale_subscription',
        'product',
    ],
    'license': 'OPL-1',
    'data': [
        'views/product_template_views.xml',
    ],
}
