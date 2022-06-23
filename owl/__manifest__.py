# -*- coding: utf-8 -*-
{
    'name': 'OWl Framework',
    'sumary': 'OWL : to add costumere type',
    'description': """
        moduel to add costumer type to the POS and contacts module
    """,
    'author': 'Odoo PS',
    'category': 'Contact',
    'version': '15.0.1.0.0',
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
