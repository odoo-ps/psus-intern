# -*- coding: utf-8 -*-
{
    "name": "Action to Confirm RFQs",
    "summary": """RFQs from the Stores to the central Stores to be confirmed into POs automatically.""",
    "description": """ In order to make sure that the client arrives in the morning and already have the RFQs to the vendors created, 
        the RFQs from the Stores to the central Stores need to be confirmed into POs automatically.
        Task ID: 2873996
        """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0",
    "license": "OPL-1",
    "depends": ["account", "product", "sale"],
    "data": [
        "data/auto_confirm.xml"
    ],
    "application": False,
}
