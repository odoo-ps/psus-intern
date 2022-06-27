# -*- coding: utf-8 -*-
{
    'name': 'Greenville product list',
    'sumary': 'Add a product list for consumers',
    'description': """
        App to add a product list for consumers
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'license': 'OPL-1',
    'data': [
        'security/ir.model.access.csv',
        'views/product_list_view.xml',
        'views/porduct_list_menu_items.xml',
        'views/contact_view_inherit.xml',
    ],
   'demo': [
   ],
}
