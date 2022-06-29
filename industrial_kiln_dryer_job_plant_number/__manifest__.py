# -*- coding: utf-8 -*-

{
    'name': 'Job numbering & Plant codes',
    'summary': 'Creates custom job numbers and plant codes',
    'description': 'Creates custom job numbers and plant codes',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'sales',
    'license': 'OPL-1',
    'version': '0.1',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views_inherit.xml',
        'security/industrial_kiln_dryer_security.xml',
        'security/ir.model.access.csv'
    ]
}  