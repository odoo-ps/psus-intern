# -*- coding: utf-8 -*-
{
    'name': 'Botelling Experts',
    'sumary': 'Add custom reports to the Bottling Experts module',
    'description': """
        App to create custom reports for Bottling Experts module, including:
        -quotation report
    """,
    'author': 'Odoo PS',
    'category': 'Reports',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
    ],
    'license': 'OPL-1',
    'data': [
        'views/sale_view_form_inherit.xml',
        'reports/quotation_report_templates.xml',
    ],
}
