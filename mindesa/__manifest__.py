# -*- coding: utf-8 -*-
{
    'name': 'Confirm RFQs ',
    'sumary': 'Confirm',
    'description': """
        Confirm RFQs
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'purchase',
    ],
    'data': [
       'views/rfqs_to_po_scheduler.xml'
    ],
    'license': 'OPL-1',
}
