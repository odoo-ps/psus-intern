# -*- coding: utf-8 -*-

{
    'name': 'Greenville Produce: Unique product lists per customer on website',
    'summary': """
            This module adds a product list assignable to customers""",
    'description': """
        Customers are only shown the products that they would buy and nothing unrelated.

        task id: 2874228
    """,
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Training',
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale', 'contacts', 'website_sale', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_list_views.xml',
        'views/contact_views.xml',
    ],
}
