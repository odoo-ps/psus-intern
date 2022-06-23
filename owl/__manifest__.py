# -*- coding: utf-8 -*-
{
    'name':'owl',

    'summary':"""Framework: POS Changes""",

    'description':"""
        Adds a field Consumer, Patient, Caregiver and External Patient       
    """,

    'author':'Odoo PS',

    'website':'https://www.odoo.com',

    'category':'Training',

    'version':'15.0.1.0.0',

    'depends':['point_of_sale'],

    'data':[
        'views/pos_assets.xml',
        'views/res_partner_view.xml',
    ],

    "assets":{
        'point_of_sale.assets':
            ['/owl/static/src/js/customer_type.js'],

        'web.assets_qweb':
            ['/owl/static/src/xml/pos_changes.xml'],
    },

}
