# -*- coding: utf-8 -*-

{
    'name': "Greenville Produce - Product List",
    'summary': """
        Customized list of products
    """,
    'description': """
        Allows customers to use a custom product list. If a product list is selected, only items belonging to the list will be shown on the shop page. Otherwise the page is displayed normally.
        Ticket: 2874041
    """,
    'author': "Odoo Inc.",
    'website': "https://www.odoo.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale','website','website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views_inherit.xml',
        'views/product_list_tag_views.xml',
        'views/partner_inherit.xml',
    ],
    'license': 'OPL-1',
}
