# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Job Numbers and Plant Codes",
    'summary': """Creates sequential job numbers and plant codes""",
    'description': """
        On sales orders, a job number will be generated from a user
        chosen prefix and an Odoo-handled sequence. Once the record
        is saved, the job number will be saved and associated with
        the record.

        On the customer form, a plant code will be generated using
        the customer's company name and an Odoo-handled sequence
        when their sales order has been confirmed. It will be saved
        once the sales order is confirmed.

        Task ID: 2873678
        """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Sales',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['sale'],
    'application': False,
    'auto_install': False
}
