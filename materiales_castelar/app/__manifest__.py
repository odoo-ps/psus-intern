# -*- coding: utf-8 -*-

{
    'name': 'Materiales Castelar',
    'summary': """Warehouse should not receive more than ordered quantity""",
    'description': """Warehouse quantity_done must be <= product_uom_qty. If the user enters a bigger quantity, warning is raised and user is prompted to enter a valid quantity.""",
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Inventory',
    'version': '15.0.1.0',
    'depends': ['stock'],
    'data': [
    ],
    'demo': [
    ],
}