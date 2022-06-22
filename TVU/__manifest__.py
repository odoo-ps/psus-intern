# -*- coding: utf-8 -*-
{
    'name': "Cancelling quotation for past expiry",

    'summary': """
        keeping the sales orders updated by cancelling already expired quotations""",

    'description': """
        This module will keep a check on the expiry date of the sales orders and cancel a quotation if it is past the current date.
    """,

    'author': "Mihir",
    'website': "http://www.odoo.com",

    'category': 'Sales',
    'version': '1.0',

    'depends': ['sale'],

    'data': [
        'data/cron_job.xml',
    ],
}
