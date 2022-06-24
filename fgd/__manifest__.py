# -*- coding: utf-8 -*-
{
    'name':'fgd',

    'summary':"""FGD Glass Solutions: Modify default access rights on contacts""",

    'description':"""
        Users of group sales/own documents only and sales/all documents can not modify salesperson and pricelists.    
    """,

    'author':'Odoo PS',

    'website':'https://www.odoo.com',

    'category':'Training',

    'version':'14.0',

    'depends':['sale_management','contacts','product',],

    'data':[
        'security/security_groups.xml',
        'views/partner_view_inherit.xml',
    ],
}
