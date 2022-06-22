# -*- coding: utf-8 -*-
{
    'name': "Fiber Mountain Product Configuration",

    'summary': 'Automatically add or retrieve products based on their configuration.',

    'description': """
        Automatically add or retrieve products based on their configuration.

        In a new quotation, when a 

        Task link:
        https://www.odoo.com/web#id=2874282&menu_id=5200&cids=3&action=4665&active_id=2874261&model=project.task&view_type=form
    """,

    'author': "Odoo Inc",
    'website': "https://odoo.com",

    'category': 'Custom Development',
    'version': '1.0',

    'depends': ['product'],

    'data': [
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/product.attribute.csv',
    ],
}
