# -*- coding: utf-8 -*-
{
    'name': "Greenville Product Lists",

    'summary': 'Manage a subset of the products.',

    'description': """
        Manage a subset of the products.
        On the website, users assigned to a product list will only see products from that list.
        Task ID: 2873979
    """,

    'author': "Odoo Inc",
    'website': "https://www.odoo.com/",
    'license': 'OPL-1',

    'category': 'Custom Development',
    'version': '1.0',
    'application': False,
    'installable': True,
    'auto_install': False,

    'depends': ['website_sale', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_lists.xml',
        'views/partner.xml'
    ],
}
