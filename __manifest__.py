# -*- coding: utf-8 -*-
{
    'name': "Sale Quotation Expiry",

    'summary': """
        Cancel expired quotations""",

    'description': """
       Automatically cancels expired quotations
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
    ],


    'license': 'OEEL-1'
}
