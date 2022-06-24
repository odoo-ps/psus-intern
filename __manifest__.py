# -*- coding: utf-8 -*-

{
    'name' : 'Luxer - Invoices',
    'summary': """Include Property Partner information in Invoice.""",
    'description': """
       #2874454
       Includes Property Partner in the Invoice.
    """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com',
    'category': 'Custom Development',
    'version': '0.1.0',
    'license' :'OPL-1',
    'depends': [
        'base', 
        'sale_subscription'
    ],
    'data': [
        'views/luxer_subscriptions_views_inherit.xml',
        'views/luxer_subscriptions_invoice_views_inherit.xml',
    ],
    'demo':[
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
    'assets': {
        
    }
}
