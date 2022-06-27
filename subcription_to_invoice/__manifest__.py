# -*- coding: utf-8 -*-
{
    "name": "Subcription To invoice",
    "summary": """Copy property from subscription to invoice delivery address""",
    "description": """
        Create a many2one field Property Partner(res.partner) that goes on Subscription. 
On creation of an invoice from a subscription, if this field is set, copy it to the delivery address. If it is blank, follow the normal behavior.
        Task ID: 2873984
        """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0",
    "license": "OPL-1",
    "depends": ["sale_subscription", "account", "sale"],
    "data": [
        "views/sale_subscription.xml"
    ],
    "application": False,
}
