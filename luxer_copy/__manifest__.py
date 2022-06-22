# -*- coding: utf-8 -*-
{
    'name': 'Luxer Copy',
    'sumary': 'Copy properties from res.partner to subscription',
    'description': """
        Copy properties from res.partner to subscription
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'sale_subscription'
    ],
    'license': 'OPL-1',
    'data': [
        'views/sale_subscription_views.xml',
    ],

}
