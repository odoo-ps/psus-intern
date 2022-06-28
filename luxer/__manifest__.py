# -*- coding: utf-8 -*-
{
    'name': 'Luxer',
    'sumary': 'Copy properties from res.partner to subscription',
    'description': """Luxer keeps track of a Contact record, Property Partner they want on each subscription. They want this field copied to the delivery address on the invoice when it is created from subscription.If it is not set, then just keep the same delivery address as normal. Task ID: 2874205""",
    'author': 'Odoo Inc',
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

}