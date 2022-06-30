# -*- coding: utf=8 -*-


{
    'name': 'GreenVille Produce',
    
    'summary': """ Unique Product lists per customer on website """,
    
    'description': """
    
        ID: 2874114

        Greenville's customers have specific needs and some of them would only ever need to see a select group of products. They only want to see products that they would buy and nothing unrelated. For example, one of Dollar General's stores only buys 5 products and they have to search for each of the 5 products while another Dollar General store may buy 10 products, unique from the first set of 5. Each customer has very specific needs and they want to make their customer experience online smoother with less hassle.
    
    """,
    
    'author': 'Odoo Inc',

    'license': 'OPL-1',

    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '14.0',

    'application': False,

    'auto-install': False,

    'installable': True,
    
    'depends': 
    [
        'sale','website_sale'
        ],
    
    'data': 
    [
        'security/ir.model.access.csv',
        'views/product_list.xml',
        'views/product_list_views_form_tree.xml',
        'views/res_partner_inherit_view.xml',
        # 'views/product_list_website_inherit_view.xml'
        ],
}