# -*- coding: utf-8 -*-

{
    'name': "TVU Networks",

    'summary': """
        Automatically cancels quotations after their expiration date has passed. 
    """,

    'description': """
        Cancels quotations in the Sales app every night at midnight after their validity date has passed
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    'category': 'Sales',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'data/quotation_auto_cancel.xml', 
    ],

    'demo': [

    ],
}
