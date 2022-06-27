# -*- coding: utf-8 -*-

{
    'name': 'Greenville Unique Product List',
    'summary': 'Creates a unique product list per client',
    'description': 'Creates a unique product list per client',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'version': '0.1',
    'depends': ['sale_management', 'website_sale', 'contacts'],
    'data': [
        'views/greenville_menuitems.xml',
        'views/product_list_views.xml',
        'security/greenville_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views_inherit_greenville.xml'
    ]
}