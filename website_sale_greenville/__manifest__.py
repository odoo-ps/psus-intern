# -*- coding: utf-8 -*-
{
    'name':'Website Sale Greenville',

    'summary':'Product lists according to clients',

    'description':"""
    Adding a product list where customers that use this list don't see any others products on website if they are not in the list already.
    Moreover, if the list is empty then users can see all the products on website.""",

    'author':'Odoo PS',

    'category':'Sales',

    'version':'14.0.1.0.0',

    'depends':[
        'sale',
        'website',
        'website_sale',
    ],

    'data':[
        'security/ir.model.access.csv',
        'views/products_menuitems.xml',
        'views/product_list_views.xml',
        'views/res_partner_views_inherit.xml',
    ],
    
    'license':'OPL-1',
}
