# -*- coding: utf-8 -*-


{
    'name': "Update Invoice Address",

    'summary': """
    Created a new field in subscription and copied it in the invoice to show as a partner
    """,
    
    'description': """
    Copy property from subscription to invoice delivery address
    """,

    'author': "Odoo Inc.",
    'website': "http://www.odoo.com",

    'category': 'Subscription',
    'version': '1.0',

    'depends': ['sale_subscription'],

    'data': [
        'views/subscription.xml',
    ],
}
