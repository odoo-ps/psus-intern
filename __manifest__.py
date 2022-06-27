# -*- coding: utf-8 -*-
{
    'name': "P&W Shoes",

    'summary': """""",

    'description': """
        Adds new fields to purcahse.template for managing shoes and calculate sale price
        """,

    'author': 'Philip Snyder',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_template_views.xml'
    ],

    'application': False,
}
