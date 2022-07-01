# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Bottling Experts: Custom PDF Reports",
    'summary': """Specialized Quotation and Invoice Templates""",
    'description': """
        Creates a custom quotation and invoice template as per the
        specifications of the client, Bottling Experts.

        Task ID: 2873668 - alac
        """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Custom Development',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['account',
                'sale',
                'purchase'],
    'application': False,
    'auto_install': False
}
