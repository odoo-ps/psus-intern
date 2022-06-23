# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes : Auto-calculated price',
    'summary': """
            This module extends product.template to include data fields such as pairs of shoes per case
            and price per pair of shoes. The list price field is calculated by the two new fields.""",
    'description': """
        This module extends product.template to include data fields such as pairs of shoes per case
        and price per pair of shoes. The list price field is calculated by the two new fields. If 
        something is entered in the pairs per case or price per pair fields, then the list price will not 
        be editable. Otherwise, the list price can be changed. 

        task id: 2874253
    """,
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Training',
    'version': '0.1',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'views/product_views_inherit.xml',
    ],
    'demo': [
        
    ],
}
