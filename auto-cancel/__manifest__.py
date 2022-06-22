# -*- coding: utf-8 -*-

{
    'name': "Auto-Cancel Expired Quotations",
    'summary': "Automatically cancel past due sales orders",
    'description': """
        Sales orders whose expiration date is before the current date
        will be automatically cancelled as they are no longer relevant.
        All expiration dates are compared at midnight (12:00 AM) of the
        designated date.

        Task ID: 2873662
    """,
    'author': "Odoo Inc.",
    'website': "https://www.odoo.com/",
    'category': 'Sales',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['sale',
                'account_taxcloud'],
    'application': False,
}
