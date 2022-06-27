# -*- coding: utf-8 -*-
{
    'name': 'Odoo Product',
    'sumary': 'Greenville Produce: Unique product lists per customer on website',
    'description': """
        odoo product helps you to create a unique product list per customer on website
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'views/greenville_menuitems.xml',
        'views/product_list_views.xml',
        'views/res_partner_views_inherit.xml',
        'security/ir.model.access.csv',
    ],
}
