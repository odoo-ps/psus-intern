# -*- coding: utf-8 -*-


{
    'name': "Copy property from subscription to invoice delivery address",

    'summary': """
    Created a new field in subscription and copied it in the invoice to show as a partner
    """,

    'author': "Mihir",
    'website': "http://www.odoo.com",

    'category': 'Subscription',
    'version': '1.0',

    'depends': ['sale_subscription'],

    'data': [
        'views/invoice.xml',
        'views/subscription.xml',
    ],
}
