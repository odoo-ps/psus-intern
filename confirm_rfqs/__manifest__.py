# -*- coding: utf-8 -*-
{
    'name': 'Confirm RFQs ',
    'sumary': 'Confirm',
    'description': """
        Confirm RFQs.
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale_subscription',
        'purchase',
    ],
    'data': [
        'views/confirm_rfqs_scheduler.xml'
    ],
    'license': 'OPL-1',
}
