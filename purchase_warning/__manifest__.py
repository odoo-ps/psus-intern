# -*- coding: utf-8 -*-

{
    "name": "Purchase Warning",
    "summary": """Materiales Castelar wants to control receipts to make sure the different warehouses won't receive more than the ordered quantity.""",
    "description": """
        In Inventory app, in Receipts, when receiving the product, quantity_done must be equal or less than the demand (product_uom_qty). 
        If the user enters a bigger quantity than the demand, 
        a warning should appear saying "You can't receive more than the ordered quantity. Please, enter another quantity". 
        This requirement is only for receipts and should work in all the different warehouses. 
        Task ID: 2873980
        """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0",
    "license": "OPL-1",
    "depends": ["stock"],
    "data": [],
    "application": False,
}
