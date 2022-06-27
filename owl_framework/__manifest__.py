# -*- coding: utf-8 -*-
{
    'name': 'Owl_framework',
    'sumary': 'OWL Framework: POS changes',
    'description': """
        [romf]: OWL Framework: POS changes
    """,
    'author': 'Odoo PoS',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': [
        'purchase',
        'point_of_sale',

    ],
    'data': [
       'views/res_partner_inherit.xml'
    ],
    "assets":{
        "web.assets_qweb":
            [
            "owl_framework/static/src/xml/CostumerType.xml",
            ],
         "point_of_sale.assets": [
             "owl_framework/static/src/js/model_inherit.js",
         ]
        },
    'license': 'OPL-1',
}
