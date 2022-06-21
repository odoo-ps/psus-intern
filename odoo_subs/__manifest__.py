# -*- coding: utf-8 -*-

{
    'name': 'Odoo Subscription',

    'summary': """Subscription app to manage the address of the invoices""",

    'description': """
        Subscription Module to invoices address
    """,

    'author': 'Odoo-psus',

    'website': 'https://www.odoo.com',

    'category': 'Subscription',

    'version': '15.0.1.0.0',

    'depends': ['sale', 'sale_subscription'],

    'license': 'OPL-1',

    'data': [
        'views/invoice_inherit.xml',
        'views/sale_subscription_inherit.xml',
        'views/sale_order_inherit.xml',
    ],

}
