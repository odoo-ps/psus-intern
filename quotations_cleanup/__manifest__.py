# -*- coding: utf-8 -*-
{
    'name': "quotations_cleanup",

    'license': 'LGPL-3',

    'summary': 'Cleanup quotations that are due to expire every midnight.',

    'description': """
        Cleanup quotations that are due to expire every midnight.
    """,

    'author': "Odoo",
    'website': "https://odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '15.0.1.0',

    'depends': ['sale'],

    'data': [
        'data/cron.xml',
    ],
}
