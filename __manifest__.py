# -*- coding: utf-8 -*-
{
    'name': "OWL Framework - POS Changes",

    'summary': """""",

    'description': """
        Add customer type selection field to backend and pos frontend.
        """,

    'author': 'Philip Snyder',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    'depends': ['point_of_sale'],

    'data':[
        'views/res_partner_views.xml',
    ],

    'assets': {
        'web.assets_qweb': [
            'owl_framework_pos_changes/static/src/xml/ClientDetailsEdit.xml',
        ],
        'point_of_sale.assets':[
            'owl_framework_pos_changes/static/src/js/models.js'
        ]

    },

    'application': False,
}
