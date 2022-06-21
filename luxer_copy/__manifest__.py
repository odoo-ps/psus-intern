# -*- coding: utf-8 -*-
{
    'name': 'Luxer Copy',
    'sumary': 'Copy properties from res.partner to subscription',
    'description': """
        Copy properties from res.partner to subscription
    """,
    'author': 'damu',
    'category': 'Sales',
    'version': '0.1',
    'depends': [
        'sale',
        'sale_subscription'
        ],
    'license': 'OPL-1',
    'data': [
        'views/sale_subscription_views_inherit.xml',
    ],
    'demo': [
    ],

}
