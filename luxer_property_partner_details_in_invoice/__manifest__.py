# -*- coding: utf-8 -*-
{
    'name': "Update Address in Invoice",

    'summary': """
        This module copies the property partner information from the subscription to the invoice """,

    'description': """
        This module copies the property partner information from the subscription to the invoice and follows the default flow of copying the Contact record info into the invoice if the property partner is not given
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
    'depends': ['sale_subscription'],

    # always loaded
    'data': [
        'views/subscription_view_inherit.xml'
    ],

    'license': 'OEEL-1'
}
