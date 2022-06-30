# -*- coding: utf-8 -*-
{
    'name': "auto-calculate-price",

    'summary': """
        Modify price to be an auto calculate field""",

    'description': """
        Add new required fields and convert sales_price to an auto calculate field. 
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    'data': [
        "views/product_template_views_inherited.xml",
    ],

    'license': 'OPL-1',
   
}