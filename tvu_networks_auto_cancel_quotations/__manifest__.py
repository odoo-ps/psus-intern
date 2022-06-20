# -*- coding: utf-8 -*-

{
    'name': 'Auto Cancel Quotations',
    'summary': 'A module to delete expired quotations each day at midnight',
    'description': """
    A module to delete expired quotations each day at midnight
    Author: yall
    Task: 2874528
    """,
    'author': 'Odoo PS',
    'category': 'sales',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
    ],
    'data': [
        'data/auto_cancel_quotations_cron.xml'
    ],
    'demo': [
    ],    
    'license': 'OPL-1'
}
