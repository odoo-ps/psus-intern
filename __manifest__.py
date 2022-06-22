# -*- coding: utf-8 -*-
{
    'name': "Luxer Subscription Contact",

    'summary': """
        Auto adds delivery address to invoices""",

    'description': """
       Adds delivery address to invoice created from a subscription
    """,

    'author': "Philip Snyder",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_subcription'],


    'license': 'OEEL-1'
}
