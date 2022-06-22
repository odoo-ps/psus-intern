# -*- coding: utf-8 -*-
{
    'name': "Auto-Cancel Expired Quotes",

    'summary': """
        This module autocancels the sales quotations which have expired """,

    'description': """
        This module autocancels the sales quotations which have expired. It creates a chron job which executes everyday at 12:00AM to check for the expired quotations and move them to canceled state
        Ticket No : 2873879
    """,

    'author': "Odoo Inc",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    
    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'data/auto_cancel_quotation_view.xml'  ],

    'license': 'OEEL-1'
}
