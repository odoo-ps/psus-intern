# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes - Calculate Sales Price',
    
    'summary': """App to calculate sales prices for orders""",
    
    'description': """
        Task ID: 2873716
        Add fields for 'pairs per case' and 'price per pair' to compute the total sales price
    """,
    
    'author': 'Odoo Inc.',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training Development',
    
    'version': '0.1',
    
    'depends': ['sale','product'],
    
    'demo' : [
    ],
    
    'data': [
        'views/product_template_views.xml',
    ],

}