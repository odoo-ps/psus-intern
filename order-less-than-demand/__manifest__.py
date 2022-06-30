# -*- coding: utf-8 -*-
{
    'name': "order-less-than-demand",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        In Inventory app, in Receipts, when receiving the product, quantity_done must be equal or less than the demand (product_uom_qty).
        If the user enters a bigger quantity than the demand, a warning should appear saying "You can't receive more than the ordered quantity.
        Please, enter another quantity". 
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    'license': 'OPL-1',
   
}
