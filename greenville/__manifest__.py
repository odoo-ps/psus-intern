# -*- coding: utf-8 -*-
{
    'name': "greenville",

    'summary': """
        """,

    'description': """

    """,

    'author': "Odoo Inc.",
    'website': "http://www.odoo.com",

    'category': 'Products',
    'version': '1.0',

    'depends': ['sale', 'account', 'website_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/custom_product_form.xml',
        'views/res_partner_form.xml',
    ],
}
