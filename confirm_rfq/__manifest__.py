# -*- coding: utf-8 -*-

{
    'name': 'Confirm RFQ',
    'summary': 'Auto confirm RFQ into purchase orders',
    'description': 'Auto confirm RFQ into purchase orders',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'license': 'OPL-1',
    'version': '0.1',
    'depends': ['purchase'],
    'data': [
        'data/confirm_rfq_cron.xml'
    ]
}