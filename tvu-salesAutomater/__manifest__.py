# -*- coding: utf=8 -*-


{
    'name': 'TVU Sales Automater',
    
    'summary': """ deletes sales after expiration date """,
    
    'description': """
    Once the current date crosses the expiration date of the sale order that quotation is automtically deleted

    TaskID: 2874120
    Link: https://www.odoo.com/web#id=2874120&cids=3&menu_id=4720&action=4665&active_id=2874112&model=project.task&view_type=form
    """,
    
    'author': 'Odoo Inc',

    'license': 'OPL-1',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',

    'application': False,

    'auto-install': True,

    'installable': True,
    
    'depends': ['sale'],
    
    'data': [
        'data/tvu_view.xml'
    ]
}