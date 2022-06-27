# -*- coding: utf-8 -*-
{
    'name': 'Glass Solutions',
    'sumary': 'Access rights changes',
    'description': """
        Give access rights over specific fields to sales persons and sales admin
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale_subscription',
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/view_partner_form_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
