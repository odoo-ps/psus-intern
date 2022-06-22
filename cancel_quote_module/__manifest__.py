# -*- coding: utf-8 -*-

{
    'name' : 'Quotation Cancel Scheduler',
    
    'summary' : """Schedules cancelation of expired quotations""",

    'description' : """
    """,

    'author' : 'Orrin',

    'website' : 'https://www.odoo.com',

    'category' : 'Training',
    'version' : '0.1',

    'depends' : ['sale'],

    'data' : [
        'data/autocancel.xml',
    ],

    'demo' : [
    ],
}
