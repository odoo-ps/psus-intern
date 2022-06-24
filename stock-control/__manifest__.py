# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Product Demand Control",
    'summary': "Prevents receiving more than the ordered quantity",
    'description': """
        Warehouses cannot receive more than the ordered quantity as
        labelled on the receipts. If a user enters a bigger quantity
        than the demand, a warning appears and prevents the user from
        completing the receipt until the value is lower than demand.

        Task ID: 2873665
    """,
    'author': "Odoo Inc.",
    'website': "https://www.odoo.com/",
    'category': 'Inventory',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['stock'],
    'application': False,
    'auto_install': True
}
