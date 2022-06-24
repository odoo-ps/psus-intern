# -*- coding: utf-8 -*-
{
    'name': "Mindesa Auto confirm RFQs",

    'summary': """
        This module is used to auto update the RFQ's of a specific partner_id and user id""",

    'description': """
        This module is used to confirm the RFQ's of a specific partner_id and user id every 20minutes
        Ticket No : 2873889
    """,

    'author': "Odoo Inc",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    
    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
       'data/purchase_order_cron.xml'
    ],

    'license': 'OEEL-1'
}
