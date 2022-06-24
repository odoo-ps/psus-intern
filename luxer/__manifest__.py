# -*- coding: utf-8 -*-

{
    'name': 'Luxer',
    'summary': 'Copy client to invoice',
    'description': 'Copies the client from a subscription to an invoice',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'version': '0.1',
    'depends': ['sale_subscription'],
    'data': [
        'views/sale_subscription_views_inherit.xml',
        'views/account_move_views_inherit.xml',
        'views/sale_order_views_inherit.xml'
    ]
}