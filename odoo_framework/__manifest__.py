# -*- coding: utf-8 -*-
{
    'name': 'Odoo Framework',
    'sumary': 'OWL Framework: POS changes',
    'description': """
        odoo framework module adds a new field to the POS screen
    """,
    'author': 'EduardoCedillo(eacm)',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'views/res_partner_inherit.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'odoo_framework/static/src/js/Custumer_type.js',
        ],
        'web.assets_qweb': [
            'odoo_framework/static/src/xml/res_partner.xml',
        ],
    },
}
