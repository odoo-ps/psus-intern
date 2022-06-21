# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': 'luxer',
    'summary': """Module copy res parner in invoice""",
    'description': """Add the parner address in the invoce with in the subscription""",
    'author': 'Odoo PS',
    'website':'https://www.odoo.com',
    'category': 'Administrative',
    'version': '15.0.1.0.0',
    'depends': [
        'sale_subscription',
        'sale',
    ],
    'data':[
        'views/subscription_inherit.xml',
        'views/sale_order_inherit.xml'
        ],
    'license' : 'OPL-1', 
}
