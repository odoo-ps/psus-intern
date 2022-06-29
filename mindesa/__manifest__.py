# -*- coding: utf-8 -*-
{
    'name':'mindesa',

    'summary':"""Customized module to automatically confirm RFQs""",

    'description':"""
        Creates a new scheduler action to automatically confirm RFQs 
    """,

    'author':'Odoo PS',

    'website':'https://www.odoo.com',

    'category':'Training',

    'version':'14.0.1.0.0',

    'depends':[
        'purchase',
        'inventory'
        ],

    'data':['views/cron_view.xml'],
}
