# -*- coding: utf-8 -*-
{
    "name": "Auto-Cancel Expired Quotations",
    "summary": """Cancel Expired Quotations """,
    "description": """
      To allow for more accurate sales reporting without creating extra administrative work, 
      we would like to automatically cancel quotations which are no longer relevant, 
      as defined by the quotation passing its expiration date.
        Task ID: 2873977
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
        "data/auto_cancel.xml"
    ],
    "application": False,
}