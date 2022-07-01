# -*- coding: utf-8 -*-

{
    'name': 'Greenville Produce',
    'summary': """ Making a new model for product lists and creating new menuitem. Gives ability to add products.""",
    'description': """
        ID: 2879282

    """,
    'Author' : 'Odoo Inc',
    'website' : 'https://www.odoo.com',
    'category' : 'Custom Development',
    'version' : '15.0.1',
    'depends': ['sale'],
    'data' : [
        'views/product_menuitems.xml',
        'views/product_listview.xml',
        'security/ir.model.access.csv',
        

    ],
    'license': "OPL-1",
    'demo': [],

}
