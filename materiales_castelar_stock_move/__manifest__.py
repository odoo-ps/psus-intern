# -*- coding: utf-8 -*-
{
    'name': 'Validate Inventory Receipts',
    'version': '1.0',
    'summary': 'Validate that warehouses do not receive more than demanded.',
    'description': """
        Validate that warehouses do not receive more than demanded.

        In the Inventory app, when editing receipts, if the quantity is set to be greater than
        the demand then an error will be raised.

        Task source: 2874272
    """,
    'author': 'Odoo Inc',
    'website': 'https://odoo.com',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': [
        'stock'
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
