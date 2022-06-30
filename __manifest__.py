# -*- coding: utf-8 -*-

{
    'name': 'TVU Network - Autocancel Expired Quotations',
    
    'summary': """App to cancel expired quotations every midnight""",
    
    'description': """
        Task ID: 2873697
        Adds a scheduled action that changes the state of expired quotations to 'Cancelled' every midnight
    """,
    
    'author': 'Odoo Inc.',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training Development',
    
    'version': '0.1',
    
    'depends': ['sale'],
    
    'demo' : [
    ],
    
    'data': [
        'views/sale_order_views.xml',
    ],

}