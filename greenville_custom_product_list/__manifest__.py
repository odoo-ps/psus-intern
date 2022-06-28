# -*- coding: utf-8 -*-
{
    'name': "Greenville Product List",

    'summary': """
        This module creates custom lists which can be assigned to customers.""",

    'description': """
        This module creates custom product lists which can be used by its customers to add directly.
        Ticket No : 2873866
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
        'security/sale_order_security.xml',
       'security/ir.model.access.csv',
       'views/sales_order.xml',
       'views/res_partner_view.xml',
       
    ],

    'license': 'OEEL-1'
}
