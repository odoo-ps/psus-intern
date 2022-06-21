# -*- coding: utf-8 -*-

{
    'name': 'Auto-Cancel Quotes',
    'summary': 'Remove quotes one the experation date has passed',
    'description': 'Remove quotes one the experation date has passed',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'version': '0.1',
    'depends': ['sale_management'],
    'data': [
        'data/expire_quotes_cron.xml'
    ],
    'demo': []
}