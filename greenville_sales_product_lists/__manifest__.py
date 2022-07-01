# -*- coding: utf-8 -*-

{
    "name": "Greenville Produce - Unique Product Lists",
    "version": "14.0.1.0",
    "description": """
    #2874441 - 
    Unique product lists per customer on website.
    """,
    "summary": "Implements the Product Lists feature for Greenville Produce, each of which can contain many products, mapped to multiple customers. Also restricts the scope of products to that on the list for a given customer.",
    "author": "Odoo Inc.",
    "website": "https://www.odoo.com",
    "license": "OPL-1",
    "category": "Custom Development",
    "depends": ["base", "contacts", "sale"],
    "data": [
        "security/greenville_security.xml",
        "security/ir.model.access.csv",
        "views/greenville_sale_menu_views_inherit.xml",
        "views/greenville_sale_product_list_views.xml",
        "views/greenville_res_partner_views_inherit.xml",
    ],
    "demo": [],
    "auto_install": False,
    "installable": True,
    "application": False,
    "assets": {},
}
