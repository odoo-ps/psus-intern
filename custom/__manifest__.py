# -*- coding:utf-8 -*-
{
    'name':"Greenville Product: Unique product lists per customer on website",
    'summary':"""A module allows user to add product list and assign custom who uses thoes product list""",
    'description':"""
        Greenville Produce: Unique product lists per customer on website
        -Add new menu item 'product list' to Sale App and in the new menu item, it allows user to 
         add product list and assign custom who uses the list
        -Task ID:2874370
    """,
    'author':'Odoo Inc',
    'category':'Custom Development',
    'license':'OPL-1',
    'version':'14.0.0.1',
    'depends':['sale','product','stock'],
      
    'data':[
        'security/product_security.xml',
        'security/ir.model.access.csv',
        'views/product_lists_view.xml',
        'views/res_partner_inherit_view.xml'    
    ],
    
    'demo':[
        
    ]      
}
