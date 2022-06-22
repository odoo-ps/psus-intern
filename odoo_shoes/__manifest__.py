# -*- coding: utf-8 -*-
{
    'name': 'Odoo Shoes',
    'sumary': 'NY P&W Shoes : Auto-calculated price',
    'description': """
        odoo shoes helps calculate the sale price when you enter the price per pair and the price per case
    """,
    'author': 'EduardoCedillo(eacm)',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'views/product_template_views_inherit.xml',
    ],
}
