# -*- coding: utf-8 -*-

{
    "name": "Product Specific Lots - Prefix for Lot numbers",
    "version": "14.0.1.0",
    "description": """
    #2874446 - 
    Product lot numbers will have prefixes based on products.
    """,
    "summary": "If Lot Number Prefix i defnied, it will automatically be appended to the lot number upon hitting the plus button or mark as done button.",
    "author": "Odoo Inc.",
    "website": "https://www.odoo.com",
    "license": "OPL-1",
    "category": "Custom Development",
    "depends": ["base", "stock", "mrp"],
    "data": ["views/psl_product_template_views_inherit.xml"],
    "demo": [],
    "auto_install": False,
    "installable": True,
    "application": False,
    "assets": {},
}
