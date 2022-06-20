# -*- coding: utf-8 -*-

{
    'name': 'Remove Expired Quotations',
    'summary': """Module to automatically cancel expired quotations""",
    'description': """
        Module to cancel expired quotations every day at midnight
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '15.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views_inherit.xml'
    ],
    'demo': [

    ],
    'license': 'OPL-1',
}
