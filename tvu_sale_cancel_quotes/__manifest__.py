# -*- coding: utf-8 -*-

{
    'name': 'TVU Networks: Auto-Cancel Expired Quotations',
    'summary': """This module automatically cancels expired quotations at midnight.""",
    'description': """
        Every night at midnight, all quotations where the expiration date is before the current day are cancelled.

        If action sees a quotation where expiration date is not set, then ignore and continue.
        
        task_id: 2874234
    """,
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Training',
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'data/auto_cancel_quotes.xml',
    ],
}
