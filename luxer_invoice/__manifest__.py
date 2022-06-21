# -*- coding: utf-8 -*-
{
    'name': 'luxer invoice',
    'sumary': 'Add delivery adress to invoice',
    'description': """
        App to add delivery adress to invoice
    """,
    'author': 'Odoo PS',
    'category': 'Invoice',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'sale_subscription',
        'account',
    ],
    'license': 'OPL-1',
    'data': [
        'views/sale_subscripcion_view_inherith.xml',
        'views/invoice_suscription_inherith.xml',
    ],
}
