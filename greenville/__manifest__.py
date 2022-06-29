# -*- coding: utf-8 -*-
{
    'name': "Greenville: Custom Product List",

    'summary': """
        Enabling Customers to create a custom product list and
        only displaying products from their customized list
    """,

    'description': """
        Taskid: 2873936
        Created a model to enable customers create a customized list.
        It can be seen which all customers are using a particular list.
        A customer is only shown products from their own customized list
        when they visit the website shop, hence making it more convenient.
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

    'license': 'OPL-1'
}
