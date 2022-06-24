#-*- coding: utf-8 -*-
{
    'name':'NY P&W Shoes : Auto-calculated price',
    
    'summary':"""A module to auto-calculate the price for NY P&W Shoes""",
    
    'description':"""
        NY P&W Shoes : Auto-calculated price
        -Create a new action to auto calculate the sales price, if pair per
         case and price per pair two fields have nothing, the sales price field
         is editable
        -Task ID:2874395
    """,
    
    'author': 'Odoo Inc',
    
    'website': 'https://www.odoo.com',
    
    'category':'Custom Development',
    'version':'15.0.1.1',
    'license': 'OPL-1', 
    'depends':['product'],

    'data':[
       'views/product_template_view.xml'
    ]       
}
