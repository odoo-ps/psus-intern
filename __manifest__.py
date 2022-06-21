# -*- coding: utf-8 -*-

{
    'name' : 'TVU Networks',
    'summary': """Cancels Expired Quotations""",
    'description': """
       Schedules a daily CRON job to clear expired Quotations.
    """,
    'author': 'odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.2',
    'license' :'LGPL-3',
    'depends': ['sale', 'base'],
    'data': [
        'views/tvu_quotation_cron_view.xml'
    ],
    'demo':[
    ],
}
