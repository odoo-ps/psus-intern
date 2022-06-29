# -*- coding: utf-8 -*-

{
    'name' : 'Greenville Produce: Unique product lists per customer on website',
    'summary' : """Creates unique product lists depending on the customer.""",
    'description' : """
        Greenvile Produce Product Lists module:
        Creates unique product lists that show different products in the shop depending on
        the customer. It does this by creating a product.list model, which holds a list of the
        products in the list and also a list of the customers which use the product.list. As a result,
        every record in res.partner can choose up to one product.list that they would like to use.
        On the front end side, the WebsiteSale module is inherited and search_product is filtered
        based on the product list of the current user.
        Developer: Orrin
        Ticket ID: 2879228
    """,
    'author' : 'Odoo Inc.',
    'website' : 'https://www.odoo.com',
    'category' : 'Custom Development',
    'version' : '1.0.1',
    'depends' : ['contacts','sale_management','website_sale'],
    'data' : [
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        'views/product_list_menu_items.xml',
        'views/res_partner_view_inherit.xml',
        'views/product_list_view.xml',
    ],
    'license' : 'OPL-1',
    'application': False,
}
