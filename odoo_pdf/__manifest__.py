# -*- coding: utf-8 -*-
{
    'name': 'Odoo PDF',
    'sumary': 'Bottling Experts: Custom Quotation and Invoice Qweb PDF Reports',
    'description': """
        odoo PDF customize the PDF report of Quotation and Invoice
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': ['sale','web'],
    'license': 'OPL-1',
    'data': [
        'views/sale_order_views_inherit.xml',
        'report/sale_order_report_templates.xml',
    ],
}
