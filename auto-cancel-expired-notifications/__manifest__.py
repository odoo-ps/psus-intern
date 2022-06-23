# -*- coding: utf-8 -*-
{
    'name': "auto-cancel-expired-notifications",

    'summary': """
        [Intern Assignment] Auto Cancel Expired Notifications""",

    'description': """
        Every night at midnight, cancel all quotations where the expiration date is before the current day
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/auto-cancel-expired-cron.xml',
    ]
}
