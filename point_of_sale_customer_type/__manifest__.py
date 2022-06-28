# -*- coding: utf-8 -*-
{
    'name': 'Point of Sale Customer Type',
    'version': '1.0',
    'description': """
        Add customer type to POS interface.

        Task ID: 2874292
    """,
    'summary': 'Add customer type to POS',
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': [
        'point_of_sale',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
    'assets': {
        'web.assets_qweb': [
            'point_of_sale_customer_type/static/src/xml/ClientDetailsEdit.xml',
        ],
        'point_of_sale.assets': [
            'point_of_sale_customer_type/static/src/js/models.js',
        ],
    }
}
