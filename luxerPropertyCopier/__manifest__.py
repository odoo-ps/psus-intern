# -*- coding: utf=8 -*-


{
    'name': 'Luxer Property Copier',
    
    'summary': """ Copy Property from subscription to invoice delivery """,
    
    'description': """
    ID: 2874127
    link: https://www.odoo.com/web#id=2874127&cids=3&menu_id=4720&action=4665&active_id=2874112&model=project.task&view_type=form

        When ever an invoice is created from subscription copy the contact record to delivery address 
    """,
    
    'author': 'Odoo Inc',

    'license': 'OPL-1',

    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',

    'application': False,

    'auto-install': True,

    'installable': True,
    
    'depends': [
        'sale_subscription',
        ],
    
    'data': [
        'views/sale_subscription_view_inherit.xml'
    ],
}