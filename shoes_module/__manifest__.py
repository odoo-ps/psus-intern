# -*- coding: utf-8 -*-

{
    'name' : 'Shoes Module',
    
    'summary' : """Handles Auto-Calculation of Shoes Fields""",

    'description' : """
    Automatically computes the sales price of a shoe product when the pair per price and
    price per pair are provided. If they aren't provided, then the sales price is directly editable.
    """,

    'author' : 'Orrin',

    'website' : 'https://www.odoo.com',

    'category' : 'Training',

    'version' : '0.1',

    'depends' : ['sale'],

    'data' : [
        'views/shoe_view.xml',
    ],

    'demo' : [
    ],

    'license' : 'LGPL-3',
}
