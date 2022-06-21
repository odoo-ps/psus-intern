# -*- coding: utf-8 -*-
{
    "name": "NY P&W Shoes : Auto-calculated price",
    "summary": """Calculate sale price based on price of each pair""",
    "description": """
        Create 2 new fields that represent the number of pair of shoes in the case
        and  the price per pair.
        Make the Sales Price uses the pair per case and price per pair to calculate the Sales price (Pair per price X Price per Pair). 
        If nothing is entered in the Pair per Case and Price per Pair, the Sales price should be editable. 
        If something is entered in Pair per Price or Price per Pair, the field should be read-only.
        Task ID: 2873996
        """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0",
    "license": "OPL-1",
    # any module necessary for this one to work correctly
    "depends": ["account", "product", "sale"],
    # always loaded
    "data": [
        "views/product_template_view.xml"
    ],
    "application": False,
}