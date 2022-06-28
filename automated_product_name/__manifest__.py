# -*- coding: utf-8 -*-
{
    "name": "Automated product name & UPC",
    "summary": """RFQs from the Stores to the central Stores to be confirmed into POs automatically.""",
    "description": """ The customer generates product names when he orders new products from the suppliers.
    The product name is a code and is linked to the product category. Those product names must be unique. The customer also needs to generate UPC automatically.
    He generates UPC and then sends it back to its manufacturer who will print it on the labels. 
    Task ID: 2873979
        """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0",
    "license": "OPL-1",
    "depends": ["purchase", "sale"],
    "data": [
        "data/product_sequence.xml",
        "data/upc_sequence.xml",
        "views/product_view_inherit.xml"
    ],
    "application": False,
}
