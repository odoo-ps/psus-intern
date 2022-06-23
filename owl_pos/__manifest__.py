# -*- coding: utf-8 -*-

{
    'name': 'POS Add Field - Customer Type',
    'summary': 'A module to add a field to the POS app, when adding a new customer or editing an existing one',
    'description': """
    A module to add a field to the POS app, when adding a new customer:

    - Displays a dropdown menu to select type of customer

    Author: yall
    Task: 2874551
    """,
    'author': 'Odoo PS',
    'category': 'pos',
    'version': '15.0.0.1',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        
    ],
    'demo':[
    ],
    'assets': {
        'point_of_sale.assets': [
            'owl_pos/static/src/js/CustomerType.js',
        ],
        'web.assets_qweb': [
            'owl_pos/static/src/xml/customer_type_template_inherit.xml',  
        ],
    },
    'license': 'OPL-1',
}
