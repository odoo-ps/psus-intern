# -*- coding: utf-8 -*-

{
    'name' : 'TVU Networks: Auto-Cancel Expired Quotations',
    'summary' : """Automatically cancels expired quotations.""",
    'description' : """
        TVU Networks module:
        Automatically cancels expired quotations, which are quotations where the 
        validity_date is older than the current date. The scheduled job runs daily
        at midnight UTC time.
        Developer: Orrin
        Ticket ID: 2879234
    """,
    'author' : 'Odoo Inc.',
    'website' : 'https://www.odoo.com',
    'category' : 'Custom Development',
    'version' : '1.0.1',
    'depends' : ['sale'],
    'data' : [
        'data/autocancel.xml',
    ],
    'license' : 'OPL-1',
    'application': False,
}
