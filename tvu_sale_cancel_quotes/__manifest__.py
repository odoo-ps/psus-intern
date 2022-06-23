# -*- coding: utf-8 -*-

{
    'name': 'TVU Networks: Auto-Cancel Expired Quotations',
    'summary': """
            To allow for more accurate sales reporting without creating extra administrative work, 
            this module will automatically cancel quotations which are no longer relevant, as defined 
            by the quotation passing its expiration date.""",
    'description': """
        Every night at midnight, all quotations where the expiration date is before the current day are cancelled.

        If action sees a quotation where expiration date is not set, then ignore and continue.
        
        task_id: 2874234
    """,
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Training',
    'version': '0.1',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'data/auto_cancel_quotes.xml',
    ],
    'demo': [
        
    ],
}
