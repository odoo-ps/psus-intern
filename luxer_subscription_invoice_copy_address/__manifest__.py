# -*- coding: utf-8 -*-

{
    'name': "Luxer - Copy Property to Invoice",
    'summary': """
        Copy property from subscription to invoice delivery address
    """,
    'description': """
        task_id: 2874346
        Inherit method '_prepare_invoice' to copy property from subscription to invoice delivery address  
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale_subscription'],
    'data': [
        'views/subscription_views_inherit.xml',
    ]
}
