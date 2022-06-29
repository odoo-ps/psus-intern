# -*- coding: utf-8 -*-

{
    'name': "Product Specific Lots",
    'summary': """
        Generate customizable lot # for manufacturing order 
    """,
    'description': """
        task_id: 2874338
        
        Added a new field 'Lot Number Prefix' for 'product.template' and corresponding field view
        Added a new field 'Lot Number' for 'mrp.production' and corresponding field view
        Inherited 'button_mark_done' method of 'mrp.production' to calculate lot number when the manufacturing order is marked done
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '0.1.0',
    'license': 'OPL-1',
    'depends': ['mrp'],
    'data': [
        'views/product_view_inherit.xml',
        'views/mrp_production_view_inherit.xml'
    ]
}
