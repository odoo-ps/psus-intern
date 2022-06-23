# -*- coding: utf-8 -*-
{
    'name': 'Owl_framework',
    'sumary': 'OWL Framework: POS changes',
    'description': """
        [romf]: OWL Framework: POS changes
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'sale_subscription',
        'purchase',
        'point_of_sale',
    ],
    'data': [
        'views/res_partner_views_inherit.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'POS_changes/static/src/js/POS_Changes.js',
        ],
        'web.assets_qweb': [
            'POS_changes/static/src/xml/CustomerType.xml',
        ],
    },
    'license': 'OPL-1',
}
