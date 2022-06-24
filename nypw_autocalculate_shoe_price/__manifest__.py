# -*- coding: utf-8 -*-

{
    'name' : 'NY P&W Shoes : Auto-calculated price',
    'summary' : """Automatically computes sales price given pair per case and price per pair.""",
    'description' : """
        NY P&W Shoes module:
        Automatically computes the sales price of a shoe product when the pair per case and
        price per pair are provided. If they aren't provided, then the sales price is directly editable.
        Developer: Orrin
        Ticket ID: 2879253
    """,
    'author' : 'Odoo Inc.',
    'website' : 'https://www.odoo.com',
    'category' : 'Custom Development',
    'version' : '1.0.1',
    'depends' : ['sale'],
    'data' : [
        'views/shoe_view.xml',
    ],
    'license' : 'OPL-1',
    'application': False,
}
