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
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_list_views.xml',
        'views/product_list_menu_views.xml',
        'views/res_partner_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
