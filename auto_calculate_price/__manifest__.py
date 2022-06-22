# -*- coding: utf-8 -*-

{
    'name': 'Auto-calculate field.',
    'summary': """Module to auto-calculate the price of a sale based on a condition.""",
    'description': """
        Sales Price - This field uses the pair per case and price per pair to calculate the Sales price (Pair per price X Price per Pair). 
        If nothing is entered in the Pair per Case and Price per Pair, the Sales price should be editable. 
        If something is entered in Pair per Price or Price per Pair, the field should be read-only. 
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '15.0.1.0.0',
    'depends': ['product'],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
