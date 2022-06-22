# -*- coding: utf-8 -*-
{
    'name': "quotations_cleanup",
    'summary': 'Auto-Cancel Expired Quotations',
    'description': 'Every night at midnight, cancels all quotations where the expiration date is before the current day.',
    'author': "Odoo",
    'category': 'Sales',
    'version': '15.0.1.0',
    'depends': ['sale'],
    'data': ['data/cron_job.xml']
}