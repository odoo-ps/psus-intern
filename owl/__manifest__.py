# -*- coding: utf-8 -*-
{
    'name': 'Mindesa Schedule',
    'sumary': 'Mindesa : Scheduled Action to Confirm RFQs',
    'description': """
        moduel to schedule the action to confirm RFQs
    """,
    'author': 'Odoo PS',
    'category': 'Purchase',
    'version': '14.0.1.0.0',
    'depends': [
        'point_of_sale',
    ],
    'license': 'OPL-1',
    'data': [
        'views/view_partner_form_inherit.xml',
    ],
    "assets": {
        'point_of_sale.assets': [
            'owl/static/src/js/costumer.js',
        ],
        "web.assets_qweb": [
            "owl/static/src/xml/client_edit.xml",
        ]},
}
