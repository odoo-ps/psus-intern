# -*- coding: utf-8 -*-

{
    'name': 'Copy personalized field into an invoice field.',
    'summary': """Module to change an invoice field by one requested by the client.""",
    'description': """
        If a field that we created is not None, then we should add it to the invoice.
        If it is None, then we should proceed as normal.
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '15.0.1.0.0',
    'depends': ['sale_subscription'],
    'data': [
        'views/sale_subscription_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
