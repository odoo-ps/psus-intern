# -*- coding: utf-8 -*-
{
    'name': "inventory_receipts_validation",

    'license': 'LGPL-3',

    'summary': "Validate that warehouse receipts don't receive more than demanded.",

    'description': """
        Validate that warehouse receipts don't receive more than demanded.
    """,

    'author': "Odoo",
    'website': "https://odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],
}
