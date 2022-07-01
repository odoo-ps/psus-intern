# -*- coding: utf-8 -*-
{
    'name': "order-less-than-demand",

    'summary': """
        Validate product quantity on receipt""",

    'description': """
        In Inventory app, in Receipts, when receiving the product, quantity_done must be equal or less than the demand (product_uom_qty). 
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    'license': 'OPL-1',
   
}
