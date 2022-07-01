# -*- coding: utf-8 -*-

{
    'name': 'Custom Quotation Report - Bottling Experts',

    'summary': """Make custom PDF quotation report for Bottling Experts""",

    'description': """
        Task ID: 2874418
        # TO BE FINISHED
    """,

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'Custom Development',

    'version': '15.0.1.0',

    'depends': ['sale'],

    'data': [
        'views/sale_views_inherit.xml',
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
    ],

    'demo': [

    ],

    'auto_install': False,

    'installable': True,

    'application': False,

    'license': 'OPL-1',
}
