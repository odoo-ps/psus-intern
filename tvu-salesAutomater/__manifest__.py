# -*- coding: utf=8 -*-


{
    'name': 'TVU Sales Automater',
    
    'summary': """ deletes sales after expiration date """,
    
    'description': """
    Once the current date crosses the expiration date of the sale order that quotation is automtically deleted
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['sale'],
    
    'data': [
        'data/tvu_view.xml'
    ],
    
    'demo': [
    ],
}