# -*- coding: utf=8 -*-


{
    'name': 'NY P&W Shoes Auto Calculated Price',
    
    'summary': """ AutoCalculating the sales price for the client """,
    
    'description': """
    ID: 2874139
    link: https://www.odoo.com/web#id=2874139&cids=3&menu_id=4720&action=4665&active_id=2874112&model=project.task&view_type=form

    The client can enter pair per case and price per pair fields in the product.template model if there is any value entered here then the sales price field will be automatically calculated or else it will be editable
    """,
    
    'author': 'Odoo Inc',

    'license': 'OPL-1',

    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',

    'application': False,

    'auto-install': False,

    'installable': True,
    
    'depends': [
        'product',
        ],
    
    'data': [
        'views/product_template_inherit_views.xml'
    ],
}