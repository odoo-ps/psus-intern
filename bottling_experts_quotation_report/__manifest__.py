# -*- coding: utf-8 -*-

{
    'name': 'Custom Quotation Report - Bottling Experts',

    'summary': """Make custom PDF quotation report for Bottling Experts""",

    'description': """
        Task ID: 2874418
        According to opinions from the company - `Bottling Experts`,
        the report template for its Order/Quotation is modified.
        Detailed description can be refered to https://www.odoo.com/web#id=2874418&cids=3&menu_id=4720&action=4665&active_id=2874404&model=project.task&view_type=form
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
