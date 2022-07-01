# -*- coding: utf=8 -*-


{
    'name': 'New York P&W Automated Product name and UPC',
    
    'summary': """ Automatically genreate product names on creation """,
    
    'description': """
    
        ID: 2874122

        1. Generate product name for each and every ordered product.
        2. Handle Uniqueness of names
        3. Create UPC and re-create the custom gender fields
    
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
        'product'
        ],
    
    'data': 
    [
        'data/ir_sequence_data.xml',
        'views/product_template_inherit_view.xml'
        ],
}