# -*- coding: utf-8 -*-

{
    'name': "TVU Networks - Autocancellation",
    'summary': """
        Automatically cancels quotations after their expiration date has passed. 
    """,
    'description': """
        Ticket 2874049: Cancels quotations in the Sales app every night at midnight after their validity date has passed
    """,
    'author': "Odoo",
    'website': "https://www.odoo.com",
    'license': 'OPL-1',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'data/quotation_auto_cancel.xml', 
    ],
    'demo': [],
}
