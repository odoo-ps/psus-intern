#-*- coding: utf-8 -*-

{
    'name':'shoes',
    
    'summary':"""manage shoes sales""",
    
    'description':"""
        manage shoes sales:
       -Distributor
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category':'Sales',
    'version':'0.1',
    'license': 'OPL-1', 
    'depends':['base','sale'],
    
    'data':[
       'views/product_template_view.xml'
    ],
    
    'demo':[
       
    ]
        
}