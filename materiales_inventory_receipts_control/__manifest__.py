# -*- coding: utf-8 -*-
{
    'name': "Materiales Inventory Receipts Control",

    'summary': """Control products in Receipts quantity_done must be equal or less than the demand""",

    'description': """
        [In Inventory app, in Receipts, when receiving the product, quantity_done must be equal or less than the demand (product_uom_qty). If the user enters a bigger quantity than the demand, a warning should appear saying "You can't receive more than the ordered quantity. Please, enter another quantity". 

        This requirement is only for receipts and should work in all the different warehouses. ]
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '14.0.1.0.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': [
        'stock',
    ],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
