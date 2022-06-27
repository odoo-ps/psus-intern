# -*- coding: utf-8 -*-

{
    'name': 'Greenville Produce Product List',
    'summary': 'A module to show the client\'s products according to their interests',
    'description': """
    A module to show the client\'s products according to their interests
    Author: yall
    task: 2874522
    """,
    'author': 'Odoo PS',
    'category': 'Website',
    'version': '14.0.0.1',
    'depends': [
        'product',
        'website',
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/products_menuitems.xml',
        'views/product_list_views.xml',
        'views/res_partner_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
