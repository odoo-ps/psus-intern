# -*- coding: utf-8 -*-

{
    'name' : 'TVU Networks - Autocancel Expired Quotations',
    'summary': """Cancels Expired Quotations""",
    'description': """
        #2874447
       Schedules a daily CRON job to clear expired Quotations.
    """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com',
    'category': 'Custom Development',
    'version': '0.1.0',
    'license' :'OPL-1',
    'depends': [
        'base', 
        'sale'
    ],
    'data': [
        'views/tvu_quotation_cron_view.xml'
    ],
    'demo':[
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
    'assets': {
        
    }
}
