# -*- coding: utf-8 -*-

{
    "name": "NY P&W Shoes - Autocalculate Sale Price",
    "version": "0.1.0",
    "description": """
    #2874466 - 
    Autocalculate Sale Price from newly created price per pair and Pair per case fields.
    """,
    "summary": "Autocalculate Sale Price from other fields.",
    "author": "Odoo Inc.",
    "website": "https://www.odoo.com",
    "license": "OPL-1",
    "category": "Custom Development",
    "depends": ["base", "stock"],
    "data": ["views/nypaw_product_template_views_inherit.xml"],
    "demo": [],
    "auto_install": False,
    "installable": True,
    "application": False,
    "assets": {},
}
